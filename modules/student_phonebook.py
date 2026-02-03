import os
import csv

# -------------------------------
# Paths
# -------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FOLDER = os.path.join(PROJECT_ROOT, "data")
FILE_PATH = os.path.join(DATA_FOLDER, "phonebook.csv")

os.makedirs(DATA_FOLDER, exist_ok=True)


# -------------------------------
# Create default dirty dataset (50 records)
# -------------------------------
def create_default_file():
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        return  # don't overwrite existing data

    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Age", "Class", "Percentage"])

        students = [
            ["Gauri", "9999999999", 20, "SY-AIML", 92.5],
            ["Rahul", "8888888888", 21, "SY-AIML", 88],
            ["Amit", "7777777777", 19, "SY-AIML", 75],
            ["Sneha", "6666666666", 20, "SY-DS", 81],
            ["Ravi", "5555555555", 22, "SY-CS", 69],
            ["Priya", "4444444444", 20, "SY-AIML", 95],
            ["Ankit", "3333333333", 21, "SY-CS", 55],
            ["Neha", "2222222222", 20, "SY-AIML", 89],
            ["Kunal", "1111111111", 19, "SY-DS", 77],
            ["Pooja", "9999999998", 20, "SY-CS", 91],

            # Duplicate
            ["Gauri", "9999999999", 20, "SY-AIML", 92.5],

            # Missing values
            ["", "9999991111", 20, "SY-AIML", 85],
            ["Sanjay", "", "", "SY-CS", 72],
            ["Meena", "8888881111", 19, "", 90],
            ["Rohit", "7777771111", 21, "SY-AIML", ""],

            # Wrong datatypes
            ["Nisha", "6666661111", "twenty", "SY-CS", 66],
            ["Arjun", "5555551111", 20, "SY-AIML", "eighty"],
            ["Divya", "4444441111", 19, 123, 74],

            # Outliers
            ["Varun", "3333331111", 20, "SY-AIML", 150],
            ["Sonal", "2222221111", 21, "SY-CS", -10],

            # Invalid class
            ["Aakash", "1111111112", 20, "UNKNOWN", 70],
            ["Tina", "9999992222", 22, "3rdYear", 83],

            # Normal records
            ["Ishita", "8888882222", 19, "SY-DS", 68],
            ["Harsh", "7777772222", 20, "SY-AIML", 79],
            ["Maya", "6666662222", 21, "SY-CS", 88],
            ["Nikhil", "5555552222", 22, "SY-AIML", 60],
            ["Asha", "4444442222", 20, "SY-CS", 73],
            ["Ramesh", "3333332222", 19, "SY-DS", 64],
            ["Kriti", "2222222223", 21, "SY-AIML", 85],
            ["Om", "1111112222", 20, "SY-CS", 90],
            ["Simran", "9999993333", 22, "SY-AIML", 71],
            ["Aditya", "8888883333", 19, "SY-DS", 78],
            ["Kavya", "7777773333", 20, "SY-AIML", 84],
            ["Manish", "6666663333", 21, "SY-CS", 59],
            ["Ritika", "5555553333", 22, "SY-DS", 92],
            ["Shubham", "4444443333", 19, "SY-AIML", 67],
            ["Deepa", "3333333334", 20, "SY-CS", 80],
            ["Suresh", "2222223333", 21, "SY-AIML", 76],
            ["Payal", "1111113333", 22, "SY-DS", 88],
            ["Vikas", "9999994444", 20, "SY-CS", 70],
            ["Komal", "8888884444", 19, "SY-AIML", 93],
            ["Rajat", "7777774444", 20, "SY-DS", 65],
            ["Nidhi", "6666664444", 21, "SY-AIML", 82],
            ["Ashwin", "5555554444", 22, "SY-CS", 74],
            ["Tanvi", "4444444445", 19, "SY-AIML", 91],
            ["Abhishek", "3333334444", 20, "SY-DS", 69],
            ["Shreya", "2222224444", 21, "SY-CS", 87],
            ["Rohan", "1111114444", 22, "SY-AIML", 72],
            ["Anjali", "9999995555", 19, "SY-DS", 79],
            ["Mohit", "8888885555", 20, "SY-CS", 66],
            ["Sakshi", "7777775555", 21, "SY-AIML", 90],
        ]

        writer.writerows(students)

    print("✅ Default dirty dataset created")


# -------------------------------
# Append Student (custom)
# -------------------------------
def add_student():
    print("\nEnter student details (you can leave blanks or wrong types for dirty effect):")
    name = input("Name: ")
    phone = input("Phone: ")
    age = input("Age: ")
    cls = input("Class: ")
    per = input("Percentage: ")

    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, age, cls, per])

    print("✅ Student added")


# -------------------------------
# Read all students
# -------------------------------
def read_students():
    if not os.path.exists(FILE_PATH):
        print("❌ File not found")
        return

    with open(FILE_PATH, "r") as f:
        reader = csv.reader(f)
        print("\n---- STUDENTS ----")
        for row in reader:
            print(row)


# -------------------------------
# Delete student by Name
# -------------------------------
def delete_student():
    if not os.path.exists(FILE_PATH):
        print("❌ File not found")
        return

    name_to_delete = input("Enter Name to delete: ")

    with open(FILE_PATH, "r") as f:
        rows = list(csv.reader(f))

    with open(FILE_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            if row and row[0] != name_to_delete:
                writer.writerow(row)

    print(f"❌ Student '{name_to_delete}' deleted if existed")


# -------------------------------
# Menu for standalone run
# -------------------------------
def menu():
    create_default_file()
    while True:
        print("\n1. Add Student")
        print("2. Read Students")
        print("3. Delete Student")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


# -------------------------------
# Run standalone
# -------------------------------
if __name__ == "__main__":
    menu()
