// =============================
// SWITCH BETWEEN DASHBOARD TOOLS
// =============================
function showTool(tool, element){

    document.getElementById("textTool").classList.add("hidden");
    document.getElementById("documentTool").classList.add("hidden");
    document.getElementById("imageTool").classList.add("hidden");
    document.getElementById("profileTool").classList.add("hidden");

    let menu = document.querySelectorAll(".menu li");
    menu.forEach(item => item.classList.remove("active"));

    element.classList.add("active");

    if(tool === "text"){
        document.getElementById("textTool").classList.remove("hidden");
    }

    if(tool === "document"){
        document.getElementById("documentTool").classList.remove("hidden");
    }

    if(tool === "image"){
        document.getElementById("imageTool").classList.remove("hidden");
    }

    if(tool === "profile"){
        document.getElementById("profileTool").classList.remove("hidden");
    }
}


// =============================
// TEXT PLAGIARISM CHECK
// =============================
async function checkText(){

    let text1 = document.getElementById("text1").value;
    let text2 = document.getElementById("text2").value;

    let res = await fetch("/check_text",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            text1:text1,
            text2:text2
        })
    });

    let data = await res.json();

    showResult(data.similarity);
}


// =============================
// DOCUMENT PLAGIARISM CHECK
// =============================
async function checkDocument(){

    let file1 = document.getElementById("docFile1").files[0];
    let file2 = document.getElementById("docFile2").files[0];

    if(!file1 || !file2){
        alert("Please upload both documents");
        return;
    }

    let formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    let res = await fetch("/check_document",{
        method:"POST",
        body:formData
    });

    let data = await res.json();

    showResult(data.similarity);
}


// =============================
// IMAGE OCR CHECK
// =============================
async function checkImage(){

    let file1 = document.getElementById("imgFile1").files[0];
    let file2 = document.getElementById("imgFile2").files[0];

    if(!file1 || !file2){
        alert("Please upload both images");
        return;
    }

    let formData = new FormData();
    formData.append("file1", file1);
    formData.append("file2", file2);

    let res = await fetch("/check_image",{
        method:"POST",
        body:formData
    });

    let data = await res.json();

    showResult(data.similarity);
}


// =============================
// SHOW RESULT FUNCTION
// (Used by Text, Document, Image)
// =============================
function showResult(similarity){

    document.getElementById("resultText").innerText =
        similarity + "% Similar";

    document.querySelector(".result").classList.add("show");

    let bar = document.getElementById("progressBar");

    bar.style.width = similarity + "%";

    bar.classList.remove("low","medium","high");

    if(similarity < 30){
        bar.classList.add("low");
    }
    else if(similarity < 70){
        bar.classList.add("medium");
    }
    else{
        bar.classList.add("high");
    }
}


// =============================
// SAVE PROFILE
// =============================
function saveProfile(){

    let name = document.getElementById("profileName").value;
    let email = document.getElementById("profileEmail").value;
    let username = document.getElementById("profileUsername").value;

    document.getElementById("sidebarName").innerText = name;

    document.getElementById("profileMessage").innerText =
    "Profile Updated Successfully ✅";
}