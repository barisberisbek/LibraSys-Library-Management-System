import os

books = {}
students = {}
borrowed_books = {}


def read_books():
    global books
    with open("books.txt", "r", encoding="utf-8") as books_file:
        for line in books_file:
            parts = line.strip().split(',')
            if len(parts) >= 4:
                isbn, book_name, author, checked_field = parts[:4]
                books[isbn] = [book_name, author, checked_field]


def read_students():
    global students
    with open("students.txt", "r", encoding="utf-8") as students_file:
        for line in students_file:
            parts = line.strip().split()
            if len(parts) >= 2:
                student_id, student_info = parts[0], parts[1:]
                students[student_id] = student_info


def read_borrowed_books():
    global borrowed_books
    with open("borrowed_books.txt", "r", encoding="utf-8") as borrowed_books_file:
        for line in borrowed_books_file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                student_id = parts[0].split()[-1]
                borrowed_books_list = parts[1].split(":")[-1].strip().split()
                borrowed_books[student_id] = borrowed_books_list


def write_books():
    with open("books.txt", "w", encoding="utf-8") as books_file:
        for isbn, details in books.items():
            books_file.write(f"{isbn},{','.join(details)}\n")


def write_students():
    with open("students.txt", "w", encoding="utf-8") as students_file:
        for student_id, details in students.items():
            students_file.write(f"{student_id} {' '.join(details)}\n")


def write_borrowed_books():
    with open("borrowed_books.txt", "w", encoding="utf-8") as borrowed_books_file:
        for student_id, borrowed in borrowed_books.items():
            borrowed_books_file.write(f"Student ID: {student_id}, Borrowed Books: {', '.join(borrowed)}\n")


def list_all_books():
    print("List of All Books in the Library:")
    for isbn, details in books.items():
        print(f"ISBN: {isbn}, Book Name: {details[0]}, Author: {details[1]}, Checked: {details[2]}")
    input("Press Enter to continue...")


def list_checked_out_books():
    print("List of Checked Out Books:")
    for isbn, details in books.items():
        if details[2] == 'T':
            print(f"ISBN: {isbn}, Book Name: {details[0]}, Author: {details[1]}")
    input("Press Enter to continue...")


def add_new_book():
    isbn = input("Enter ISBN: ")
    if isbn in books:
        print("A book with the same ISBN already exists. Cannot add the book.")
        input("Press Enter to continue...")
        return

    book_name = input("Enter Book Name: ")
    author = input("Enter Author: ")
    checked_status = 'F'
    books[isbn] = [book_name, author, checked_status]
    write_books()
    print("Book added successfully!")
    input("Press Enter to continue...")


def delete_book():
    isbn_to_delete = input("Enter ISBN of the book to delete: ")
    if isbn_to_delete in books:
        if books[isbn_to_delete][2] == 'F':
            del books[isbn_to_delete]
            write_books()
            print("Book deleted successfully.")
        else:
            print("Cannot delete a checked-out book.")
    else:
        print("Book not found.")
    input("Press Enter to continue...")


def search_by_isbn():
    search_isbn = input("Enter ISBN to search: ")
    if search_isbn in books:
        details = books[search_isbn]
        print(f"ISBN: {search_isbn}, Book Name: {details[0]}, Author: {details[1]}, Checked: {details[2]}")
    else:
        print("Book not found.")
    input("Press Enter to continue...")


def search_by_name():
    search_name = input("Enter a keyword to search in book names: ")
    found = False
    for isbn, details in books.items():
        if search_name.lower() in details[0].lower():
            found = True
            print(f"ISBN: {isbn}, Book Name: {details[0]}, Author: {details[1]}, Checked: {details[2]}")
    if not found:
        print("No books found.")
    input("Press Enter to continue...")


def check_out_book():
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Invalid student ID.")
        input("Press Enter to continue...")
        return

    isbn = input("Enter ISBN of the book to check out: ")
    if isbn in books:
        if books[isbn][2] == 'F':
            books[isbn][2] = 'T'

            if student_id not in borrowed_books:
                borrowed_books[student_id] = [isbn]
            else:
                borrowed_books[student_id].append(isbn)

            write_books()
            write_borrowed_books()
            print("Book checked out successfully!")
        else:
            print("Book is already checked out.")
    else:
        print("Invalid ISBN.")
    input("Press Enter to continue...")


def list_students_and_books():
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}, Name: {' '.join(student_info)}")
        checked_books = [f"ISBN: {isbn}, Book Name: {details[0]}, Author: {details[1]}"
                         for isbn, details in books.items()
                         if details[2] == 'T' and len(details) > 2 and borrowed_books.get(student_id) and isbn in
                         borrowed_books[student_id]]
        if checked_books:
            print("Books Checked Out:")
            for book in checked_books:
                print(book)
        else:
            print("No books checked out.")
        print("\n")
    input("Press Enter to continue...")


def return_book():
    isbn = input("Enter ISBN of the book to return: ")
    if isbn in books:
        if books[isbn][2] == 'T':
            books[isbn][2] = 'F'
            if borrowed_books:
                for student_id, borrowed in list(borrowed_books.items()):
                    if isbn in borrowed:
                        borrowed.remove(isbn)
                        if not borrowed:
                            del borrowed_books[student_id]
            write_books()
            write_borrowed_books()
            print("Book returned successfully!")
        else:
            print("This book is not checked out.")
    else:
        print("Invalid ISBN.")
    input("Press Enter to continue...")


def list_all_students():
    if not students:
        print("No students found.")
        input("Press Enter to continue...")
        return

    print("List of All Students:")
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}, Name: {' '.join(student_info)}")

    input("Press Enter to continue...")


def add_student():
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists. Cannot add the student.")
        input("Press Enter to continue...")
        return

    student_name = input("Enter Student Name: ")
    student_info = [student_name]
    students[student_id] = student_info
    write_students()
    print("Student added successfully!")
    input("Press Enter to continue...")


def delete_student():
    student_id = input("Enter Student ID to delete: ")
    if student_id in students:
        # Check if the student borrowed any books
        if student_id in borrowed_books:
            # Loop through the borrowed books and update their status in 'books'
            for isbn in borrowed_books[student_id]:
                if isbn in books:
                    # Change the 'checked' status to 'F' (False)
                    books[isbn][2] = 'F'

        # Delete the student from 'students' and 'borrowed_books'
        del students[student_id]
        if student_id in borrowed_books:
            del borrowed_books[student_id]

        # Write the updated details to the files
        write_students()
        write_borrowed_books()
        write_books()

        print("Student deleted successfully.")
    else:
        print("Student not found.")
    input("Press Enter to continue...")


def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n"
          "♦                WELCOME TO THE LIBRARY APPLICATION                     ♦\n"
          "♦   •••Choose an option (1-9) or press 'q' to quit•••                   ♦\n"
          "♦  1) List all the books in the library.                                ♦\n"
          "♦  2) List all the checked out books.                                   ♦\n"
          "♦  3) Add a new book.                                                   ♦\n"
          "♦  4) Delete a book.                                                    ♦\n"
          "♦  5) Search a book by ISBN number.                                     ♦\n"
          "♦  6) Search a book by name.                                            ♦\n"
          "♦  7) Check out a book to a student.                                    ♦\n"
          "♦  8) List all the students and their checked-out books.                ♦\n"
          "♦  9) Return the checked-out books.                                     ♦\n"
          "♦  10) List all the students                                            ♦\n"
          "♦  11) Add a new student                                                ♦\n"
          "♦  12) Delete a student                                                 ♦\n"
          "♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")


def main():
    while True:
        show_menu()
        choice = input("Enter the number of the operation you want to perform or 'q' to quit: ")

        if choice == "1":
            list_all_books()
        elif choice == "2":
            list_checked_out_books()
        elif choice == "3":
            add_new_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_by_isbn()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            check_out_book()
        elif choice == "8":
            list_students_and_books()
        elif choice == "9":
            return_book()
        elif choice == "10":
            list_all_students()
        elif choice == "11":
            add_student()
        elif choice == "12":
            delete_student()
        elif choice.lower() == "q":
            write_books()
            write_students()
            write_borrowed_books()
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    read_books()
    read_students()
    read_borrowed_books()
    main()
