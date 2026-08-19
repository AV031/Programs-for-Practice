class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"\n{self.name} borrowed '{book.title}'.")
        else:
            print(f"\n'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"\n{self.name} returned '{book.title}'.")
        else:
            print(f"\n{self.name} has not borrowed '{book.title}'.")

    def view_books(self):
        print(f"\nBooks borrowed by {self.name}:")

        if not self.borrowed_books:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title}")


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Status: {status}"
        )


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\nBook '{book.title}' added successfully.")

    def add_student(self, student):
        self.students.append(student)
        print(f"\nStudent '{student.name}' added successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def issue_book(self, student_id, book_id):
        student = self.find_student(student_id)
        book = self.find_book(book_id)

        if student is None:
            print("\nStudent not found.")
            return

        if book is None:
            print("\nBook not found.")
            return

        student.borrow_book(book)

    def return_book(self, student_id, book_id):
        student = self.find_student(student_id)
        book = self.find_book(book_id)

        if student is None:
            print("\nStudent not found.")
            return

        if book is None:
            print("\nBook not found.")
            return

        student.return_book(book)

    def display_books(self):
        print("\n========== ALL BOOKS ==========")

        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_info()

    def display_students(self):
        print("\n========== ALL STUDENTS ==========")

        if not self.students:
            print("No students registered.")
        else:
            for student in self.students:
                print(
                    f"ID: {student.student_id} | "
                    f"Name: {student.name} | "
                    f"Books Borrowed: {len(student.borrowed_books)}"
                )


# ==========================================
# MAIN PROGRAM
# ==========================================

library = Library("Central Library")

while True:

    print("\n")
    print("========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Student")
    print("2. Add Book")
    print("3. Display All Books")
    print("4. Display All Students")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. View Student's Books")
    print("8. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")

        student = Student(student_id, name)
        library.add_student(student)

    # Add Book
    elif choice == "2":

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    # Display Books
    elif choice == "3":

        library.display_books()

    # Display Students
    elif choice == "4":

        library.display_students()

    # Issue Book
    elif choice == "5":

        student_id = int(input("Enter Student ID: "))
        book_id = int(input("Enter Book ID: "))

        library.issue_book(student_id, book_id)

    # Return Book
    elif choice == "6":

        student_id = int(input("Enter Student ID: "))
        book_id = int(input("Enter Book ID: "))

        library.return_book(student_id, book_id)

    # View Student's Books
    elif choice == "7":

        student_id = int(input("Enter Student ID: "))

        student = library.find_student(student_id)

        if student:
            student.view_books()
        else:
            print("\nStudent not found.")

    # Exit
    elif choice == "8":

        print("\nThank you for using the Library Management System!")
        break

    else:
        print("\nInvalid choice. Please try again.")