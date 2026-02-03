# 📘 Student Data Management & Analysis Project

## 📌 Project Overview

This project is a **Student Data Management and Analysis System** built using Python. It demonstrates core concepts of:

* File handling (CSV)
* Data cleaning & preprocessing
* Data visualization
* Modular Python programming

The project is designed as an **internship-level academic project** and is suitable for showcasing Python and Data Science skills.

---

## 📂 Folder Structure

```
student_project/
│
├── main.py                  # Main menu-driven program
├── modules/
│   ├── __init__.py
│   ├── student_phonebook.py # Student CRUD operations & dataset generator
│   ├── clean_data.py         # Data cleaning module
│   └── visualize.py           # Data visualization module
│
├── data/
│   ├── phonebook.csv           # Raw dataset (dirty data)
│   └── cleaned_phonebook.csv   # Cleaned dataset output
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

### ✅ 1. Student Phonebook System

* Add student records
* View all students
* Delete student by name
* Automatically generates a **dirty dataset** with:

  * Missing values
  * Duplicate records
  * Wrong datatypes
  * Outliers
  * Invalid class labels

---

### 🧹 2. Data Cleaning Module

The cleaning module performs:

* Removal of duplicate records
* Filling missing names with **"Unknown"**
* Validation of phone numbers (10-digit check)
* Conversion of wrong datatypes (Age, Percentage)
* Handling missing numeric values using mean
* Fixing outliers using mean of valid data
* Converting invalid class labels to standard classes
* Saving cleaned data to a **new CSV file**

---

### 📊 3. Data Visualization Module

The visualization module generates:

* Line plot (Age vs Percentage)
* Bar chart (Class-wise average percentage)
* Histogram (Age distribution)
* Correlation heatmap (Age vs Percentage)

---

## 🧑‍💻 Technologies Used

* Python 3.x
* Pandas
* Matplotlib
* Seaborn
* CSV File Handling

---

## ▶️ How to Run the Project

### 1️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Main Program

```bash
python main.py
```

---

## 📋 Menu Options

```
1. Phonebook System
2. Clean Dataset
3. Visualize Data
4. Exit
```

---

## 📈 Sample Output

* Raw dataset stored in: `data/phonebook.csv`
* Cleaned dataset stored in: `data/cleaned_phonebook.csv`
* Graphs displayed using Matplotlib

---

## 🎓 Learning Outcomes

This project demonstrates:

* Modular programming in Python
* Real-world dirty dataset handling
* Data preprocessing techniques
* Basic exploratory data analysis (EDA)
* Data visualization concepts

---

## 📌 Future Enhancements

* GUI interface using Tkinter or Streamlit
* Database storage (MySQL / SQLite)
* Machine learning model for student performance prediction
* Web-based dashboard

---

## 👩‍🎓 Author

**Gauri Nagpure**

Internship Project – Python & Data Science

---

## 📜 License

This project is for educational purposes only.
