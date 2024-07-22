										Table of Contents for the Document
     // 1 \\	
* Introduction *
 Overview
 How to Run
 Usage
		// 2 \\
	** Launch and Interaction **
	Data Structures Used
	Important Notes
	File Formats
				   // 3 \\	
			*** Functions and Features ***
			List all the books in the library
			List all the books that are checked out
			Add a new book
			Delete a book if it is not checked out. If it is checked out, give a warning message only
			Search a book by ISBN number
			Search a book by name
			Check out a book to a student
			List all the students. If a student checked out books, you should list those books under their names

						 // 4 \\
					**** Functions Overview ****
					Books
					Book Checkout
					Students
					Menu Display and Input
					Main Function





// 1 \\

Library Management System
This Python-based Library Management System provides a versatile platform for efficient management of books, students, and book borrowing within a library context.

Overview
The program employs Python's capabilities to provide a user-friendly interface for managing library resources effectively. 

How to Run
***Ensure TXTs in the Same Directory: Place the text files books.txt, students.txt, and borrowed_books.txt in the same directory as the main script mylibrary.py.
***Execution: Open a terminal or command prompt, navigate to the project directory, and execute the program using:"python main.py" 

                                                  OR

***Extract the folder inside the compressed zip file downloaded via DYS.
***To open the project, simply drag and drop the folder onto the PyCharm IDE icon. This action will initiate the project setup.
***Once the project is opened in PyCharm, navigate to the 'play' icon and click 'run.' The user interface will guide you through the available menu options.





// 2 \\

Usage
*Launch the program as instructed above.
*Interact with the menu system by entering corresponding numeric choices to execute various library management operations.
*Utilize the provided functionalities to manage books, students, borrowing, and returns efficiently within the library.


Data Structures Used
*books: A dictionary structure containing book information indexed by ISBN numbers.A dictionary storing book information with ISBN as keys and book details as values.
*students: A dictionary structure holding student details indexed by unique 6-digit student IDs.A dictionary holding student information with student IDs as keys and corresponding details as values.
*borrowed_books: A dictionary mapping student IDs to a list of borrowed book ISBNs.A dictionary storing information about books borrowed by students, using student IDs as keys and lists of borrowed book ISBNs as values.


Important Notes
*File Integrity: Ensure the correct formatting and structure of the students.txt, books.txt, and borrowed_books.txt files for proper functioning of the system.
*User Interface: The program boasts a user-friendly menu-based interface, ensuring ease of navigation and data input. It clears the screen between user inputs to enhance readability.



File Formats
*students.txt: This file comprises lines containing a 6-digit ID, followed by the student's first and last name, separated by spaces. For instance: 	123456 John Doe
*books.txt: This file contains lines with book details, each separated by commas. Each line follows the format: ISBN number, book name, author name, and a checked field denoted by 'T' for true (if the book is checked out) or 'F' for false (if the book is available). For instance: 	0385472579,Book Title,Author Name,T
*borrowed_books.txt: This file contains information about books borrowed by students. Each line represents a student's borrowing record, consisting of the student's 6-digit ID followed by a list of borrowed book ISBNs, separated by commas.
For example 123456,013284737X,0385472579


// 3 \\


Functions and Features

1)List all the books in the library
The "list_all_books()" function displays a complete list of all books available in the library. It iterates through the "books" dictionary, showing details such as ISBN, book name, author, and the checked status for each book.

2)List all the books that are checked out
The "list_checked_out_books()" function generates a list of books currently checked out. It scans the "books" dictionary, identifies books with a 'T' (indicating checked out) status, and exhibits their details.

3)Add a new book 
The "add_new_book()" function facilitates the addition of a new book to the library. It prompts users for the book's ISBN, name, and author. To ensure uniqueness, it checks if the provided ISBN already exists in the library. If the ISBN is unique, the function adds the new book's details to the "books" dictionary. Subsequently, it writes the book's information into the "books.txt" file, preventing duplicate entries and maintaining the library's inventory.

4)Delete a book if it is not checked out. If it is checked out, give a warning message only
The "delete_book()" function removes a book from the library if it's available (not checked out). It prompts the user to input the book's ISBN and then verifies its existence and checked status. If the book's status is 'F' (indicating it's available), it is deleted from the library. However, if the book is checked out ('T' status), the function displays a warning message, preventing its deletion.

5)Search a book by ISBN number
The "search_by_isbn()" function enables users to search for a book by its ISBN. By accepting an ISBN input, it checks the "books" dictionary for a match and displays the book's details if found

6)Search a book by name(e.g. if python is entered for a name, you should list all the books where their names contain the word python)
The functionality for searching by name allows users to find books using a keyword present in the book names. It uses the "search_name.lower()" function to ensure a case-insensitive search. Within a loop, the "search_by_name()" function checks for books containing the provided keyword within their names in the books dictionary.

7)Check out a book to a student.(Hint: This option can take student id and ISBN number as parameters) 
The "check_out_book()" function allows users to check out a book by providing their student ID along with the book's ISBN. It validates these inputs and, if valid, changes the book's status to 'T' (indicating it's checked out) within the books.txt file. Additionally, it updates the borrowed_books.txt file with the book's ISBN assigned to the respective student ID.

8)List all the students. If a student checked out books, you should list those books under their names.
The "list_students_and_books()" function lists all students and the books they have checked out. It loops through the "students" dictionary, checks for borrowed books in the "borrowed_books" dictionary, and displays students' details along with any borrowed book information.




// 4 \\

*Books
List All Books (list_all_books): Displays a list of all books in the library.
List Checked Out Books (list_checked_out_books): Displays books that are checked out.
Add New Book (add_new_book): Allows adding a new book to the library.
Delete Book (delete_book): Removes a book from the library if it's not checked out.
Search by ISBN (search_by_isbn): Searches for a book by its ISBN number.
Search by Name (search_by_name): Searches for a book by its name or keyword.

*Book Checkout
Check Out Book (check_out_book): Allows a student to check out a book.
Return Book (return_book): Facilitates the return of a checked-out book.

*Students
List Students and Books (list_students_and_books): Lists all students and their checked-out books.
List All Students (list_all_students): Displays a list of all students.
Add Student (add_student): Adds a new student to the library.
Delete Student (delete_student): Deletes a student from the library and their associated books if any.

*Menu Display and Input
Show Menu (show_menu): Displays a menu of options for users to interact with the library system.
Main Function (main): Controls the flow of the program based on user input from the menu.
