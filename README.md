# LibraSys: Library Management System

LibraSys is a comprehensive library management system designed with a user-friendly interface and advanced Python features. This application facilitates the tracking of books and students in the library, efficiently manages book borrowing and returning processes, and offers users various search and listing options.

## Table of Contents

1. [Introduction](#introduction)
   - [Overview](#overview)
   - [How to Run](#how-to-run)
   - [Usage](#usage)
2. [Initialization and Interaction](#initialization-and-interaction)
   - [Data Structures Used](#data-structures-used)
   - [Important Notes](#important-notes)
   - [File Formats](#file-formats)
3. [Functions and Features](#functions-and-features)
4. [Functions Overview](#functions-overview)

## Introduction

### Overview

LibraSys is a Python-based Library Management System. It provides a user-friendly interface for effective management of library resources.

### How to Run

1. Clone the project from GitHub:
git clone https://github.com/your-username/LibraSys.git
cd LibraSys

2. Place the text files in the same directory as the main script.

3. Run the following command in the terminal:
python main.py

Alternatively:
- Extract the ZIP file and drag the folder onto PyCharm.
- Click the 'play' icon in PyCharm to run.

### Usage

- Start the program and follow the menu options.
- Enter the corresponding numerical choices to perform library management operations.

## Initialization and Interaction

### Data Structures Used

- `books`: A dictionary containing book information indexed by ISBN numbers.
- `students`: A dictionary holding student details indexed by unique student IDs.
- `borrowed_books`: A dictionary mapping student IDs to a list of borrowed book ISBNs.

### Important Notes

- File integrity: Proper formatting of `students.txt`, `books.txt`, and `borrowed_books.txt` is crucial.
- User interface: The program features a menu-based interface for easy navigation.

### File Formats

- `students.txt`: Each line follows the format "123456 John Doe".
- `books.txt`: Each line follows the format "0385472579,Book Title,Author Name,T/F".
- `borrowed_books.txt`: Each line follows the format "123456,013284737X,0385472579".

## Functions and Features

1. List all books in the library
2. List all checked out books
3. Add a new book
4. Delete a book (if not checked out)
5. Search a book by ISBN
6. Search a book by name
7. Check out a book to a student
8. List all students and their checked-out books
9. Return checked-out books
10. List all students
11. Add a new student
12. Delete a student

## Functions Overview

### Books
- List all books
- List checked out books
- Add new book
- Delete book
- Search by ISBN
- Search by name

### Book Checkout
- Check out book
- Return book

### Students
- List students and their books
- List all students
- Add student
- Delete student

### Menu Display and Input
- Show menu
- Main function

This library management system ensures effective management of books and students. With its user-friendly interface and comprehensive features, it simplifies and streamlines library operations.
