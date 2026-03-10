from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import docx
import PyPDF2
from PIL import Image
import pytesseract

# SET TESSERACT PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__, template_folder="templates", static_folder="static")


# -------------------
# Helper Functions
# -------------------

def preprocess(text):

    if not text:
        return ""

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text


def calculate_similarity(text1, text2):

    text1 = preprocess(text1)
    text2 = preprocess(text2)

    vectorizer = TfidfVectorizer()

    tfidf = vectorizer.fit_transform([text1, text2])

    similarity = cosine_similarity(tfidf[0], tfidf[1])

    return round(similarity[0][0] * 100, 2)


def read_docx(file):

    doc = docx.Document(file)

    return "\n".join([para.text for para in doc.paragraphs])


def read_pdf(file):

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text


def read_image(file):

    img = Image.open(file)

    return pytesseract.image_to_string(img)


# -------------------
# Routes
# -------------------

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/index")
def index():
    return render_template("index.html")


# TEXT CHECK
@app.route("/check_text", methods=["POST"])
def check_text():

    data = request.get_json()

    similarity = calculate_similarity(
        data["text1"],
        data["text2"]
    )

    return jsonify({"similarity": similarity})


# DOCUMENT CHECK
@app.route("/check_document", methods=["POST"])
def check_document():

    if "file1" not in request.files or "file2" not in request.files:
        return jsonify({"error": "Files not uploaded"}), 400

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    # Read first file
    if file1.filename.endswith(".docx"):
        text1 = read_docx(file1)
    elif file1.filename.endswith(".pdf"):
        text1 = read_pdf(file1)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    # Read second file
    if file2.filename.endswith(".docx"):
        text2 = read_docx(file2)
    elif file2.filename.endswith(".pdf"):
        text2 = read_pdf(file2)
    else:
        return jsonify({"error": "Unsupported file format"}), 400

    similarity = calculate_similarity(text1, text2)

    return jsonify({"similarity": similarity})


# IMAGE OCR CHECK
@app.route("/check_image", methods=["POST"])
def check_image():

    if "file1" not in request.files or "file2" not in request.files:
        return jsonify({"error": "Images not uploaded"}), 400

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    text1 = read_image(file1)
    text2 = read_image(file2)

    similarity = calculate_similarity(text1, text2)

    return jsonify({"similarity": similarity})


if __name__ == "__main__":
    app.run(debug=True)