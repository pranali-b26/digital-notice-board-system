import json
import datetime

FILE = "notices.json"


# Load notices from file
def load_notices():
    try:
        file = open(FILE, "r")
        data = json.load(file)
        file.close()
        return data
    except:
        return []


# Save notices
def save_notices(data):
    file = open(FILE, "w")
    json.dump(data, file, indent=4)
    file.close()


# Admin Login
def admin_login():

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful\n")
        return True

    else:
        print("Invalid Username or Password")
        return False


# Add Notice
def add_notice():

    notices = load_notices()

    title = input("Enter Notice Title: ")
    category = input("Enter Category: ")
    message = input("Enter Message: ")

    date = str(datetime.date.today())

    notice = {
        "title": title,
        "category": category,
        "message": message,
        "date": date
    }

    notices.append(notice)

    save_notices(notices)

    print("Notice Added Successfully")


# View Notices (Table Format)
def view_notices():

    notices = load_notices()

    if len(notices) == 0:
        print("No Notices Available")
        return

    notices.sort(key=lambda x: x["date"], reverse=True)

    print("\n------------- NOTICE BOARD -------------")
    print("ID\tTITLE\t\tCATEGORY\tDATE")
    print("----------------------------------------")

    i = 1

    for n in notices:

        print(i, "\t", n["title"], "\t\t", n["category"], "\t\t", n["date"])

        i = i + 1


# Latest Notice
def latest_notice():

    notices = load_notices()

    if len(notices) == 0:
        print("No Notices Available")
        return

    notices.sort(key=lambda x: x["date"], reverse=True)

    n = notices[0]

    print("\n***** LATEST NOTICE *****")
    print("Title:", n["title"])
    print("Category:", n["category"])
    print("Message:", n["message"])
    print("Date:", n["date"])


# Search Notice
def search_notice():

    keyword = input("Enter Title or Category to Search: ").lower()

    notices = load_notices()

    found = False

    for n in notices:

        if keyword in n["title"].lower() or keyword in n["category"].lower():

            print("\nTitle:", n["title"])
            print("Category:", n["category"])
            print("Message:", n["message"])
            print("Date:", n["date"])

            found = True

    if not found:
        print("Notice Not Found")


# Update Notice
def update_notice():

    notices = load_notices()

    title = input("Enter Notice Title to Update: ")

    for n in notices:

        if n["title"] == title:

            new_message = input("Enter New Message: ")

            n["message"] = new_message

            save_notices(notices)

            print("Notice Updated Successfully")

            return

    print("Notice Not Found")


# Delete Notice
def delete_notice():

    notices = load_notices()

    title = input("Enter Notice Title to Delete: ")

    for n in notices:

        if n["title"] == title:

            notices.remove(n)

            save_notices(notices)

            print("Notice Deleted Successfully")

            return

    print("Notice Not Found")


# Dashboard
def dashboard():

    print("\n========== DIGITAL NOTICE BOARD ==========")
    print("1 Add Notice")
    print("2 View Notices (Table)")
    print("3 Latest Notice")
    print("4 Search Notice")
    print("5 Update Notice")
    print("6 Delete Notice")
    print("7 Exit")


# Main Program
if admin_login():

    while True:

        dashboard()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_notice()

        elif choice == "2":
            view_notices()

        elif choice == "3":
            latest_notice()

        elif choice == "4":
            search_notice()

        elif choice == "5":
            update_notice()

        elif choice == "6":
            delete_notice()

        elif choice == "7":
            print("Program Closed")
            break

        else:
            print("Invalid Choice")