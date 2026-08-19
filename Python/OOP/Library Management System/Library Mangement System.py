import sqlite3


# ==========================================
# DATABASE CLASS
# ==========================================

class Database:

    def __init__(self, db_name="library.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):

        # Students table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

        # Books table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_available INTEGER DEFAULT 1
            )
        """)

        # Borrowed books table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrowed_books (
                student_id INTEGER,
                book_id INTEGER,

                FOREIGN KEY (student_id)
                    REFERENCES students(student_id),

                FOREIGN KEY (book_id)
                    REFERENCES books(book_id),

                PRIMARY KEY (student_id, book_id)
            )
        """)

        self.connection.commit()

    # ==========================================
    # STUDENT OPERATIONS
    # ==========================================

    def add_student(self, student_id, name):

        try:
            self.cursor.execute("""
                INSERT INTO students (student_id, name)
                VALUES (?, ?)
            """, (student_id, name))

            self.connection.commit()

            print(f"\nStudent '{name}' added successfully.")

        except sqlite3.IntegrityError:
            print("\nStudent ID already exists.")

    def find_student(self, student_id):

        self.cursor.execute("""
            SELECT student_id, name
            FROM students
            WHERE student_id = ?
        """, (student_id,))

        return self.cursor.fetchone()

    def display_students(self):

        self.cursor.execute("""
            SELECT student_id, name
            FROM students
            ORDER BY student_id
        """)

        students = self.cursor.fetchall()

        print("\n========== ALL STUDENTS ==========")

        if not students:
            print("No students registered.")

        else:
            for student_id, name in students:

                self.cursor.execute("""
                    SELECT COUNT(*)
                    FROM borrowed_books
                    WHERE student_id = ?
                """, (student_id,))

                count = self.cursor.fetchone()[0]

                print(
                    f"ID: {student_id} | "
                    f"Name: {name} | "
                    f"Books Borrowed: {count}"
                )

    # ==========================================
    # BOOK OPERATIONS
    # ==========================================

    def add_book(self, book_id, title, author):

        try:
            self.cursor.execute("""
                INSERT INTO books
                (book_id, title, author, is_available)
                VALUES (?, ?, ?, 1)
            """, (book_id, title, author))

            self.connection.commit()

            print(f"\nBook '{title}' added successfully.")

        except sqlite3.IntegrityError:
            print("\nBook ID already exists.")

    def find_book(self, book_id):

        self.cursor.execute("""
            SELECT book_id, title, author, is_available
            FROM books
            WHERE book_id = ?
        """, (book_id,))

        return self.cursor.fetchone()

    def display_books(self):

        self.cursor.execute("""
            SELECT book_id, title, author, is_available
            FROM books
            ORDER BY book_id
        """)

        books = self.cursor.fetchall()

        print("\n========== ALL BOOKS ==========")

        if not books:
            print("No books available.")

        else:
            for book_id, title, author, is_available in books:

                status = "Available" if is_available else "Borrowed"

                print(
                    f"ID: {book_id} | "
                    f"Title: {title} | "
                    f"Author: {author} | "
                    f"Status: {status}"
                )

    # ==========================================
    # ISSUE BOOK
    # ==========================================

    def issue_book(self, student_id, book_id):

        # Check student
        student = self.find_student(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        # Check book
        book = self.find_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        book_id, title, author, is_available = book

        # Check availability
        if not is_available:
            print(f"\n'{title}' is already borrowed.")
            return

        # Insert borrowing record
        self.cursor.execute("""
            INSERT INTO borrowed_books
            (student_id, book_id)
            VALUES (?, ?)
        """, (student_id, book_id))

        # Update book availability
        self.cursor.execute("""
            UPDATE books
            SET is_available = 0
            WHERE book_id = ?
        """, (book_id,))

        self.connection.commit()

        print(f"\n{student[1]} borrowed '{title}'.")

    # ==========================================
    # RETURN BOOK
    # ==========================================

    def return_book(self, student_id, book_id):

        # Check student
        student = self.find_student(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        # Check book
        book = self.find_book(book_id)

        if book is None:
            print("\nBook not found.")
            return

        # Check whether student borrowed the book
        self.cursor.execute("""
            SELECT *
            FROM borrowed_books
            WHERE student_id = ?
            AND book_id = ?
        """, (student_id, book_id))

        borrowed = self.cursor.fetchone()

        if borrowed is None:
            print(
                f"\n{student[1]} has not borrowed "
                f"'{book[1]}'."
            )
            return

        # Delete borrowing record
        self.cursor.execute("""
            DELETE FROM borrowed_books
            WHERE student_id = ?
            AND book_id = ?
        """, (student_id, book_id))

        # Make book available again
        self.cursor.execute("""
            UPDATE books
            SET is_available = 1
            WHERE book_id = ?
        """, (book_id,))

        self.connection.commit()

        print(f"\n{student[1]} returned '{book[1]}'.")

    # ==========================================
    # VIEW STUDENT'S BOOKS
    # ==========================================

    def view_student_books(self, student_id):

        student = self.find_student(student_id)

        if student is None:
            print("\nStudent not found.")
            return

        print(f"\nBooks borrowed by {student[1]}:")

        self.cursor.execute("""
            SELECT
                b.book_id,
                b.title,
                b.author
            FROM books b
            JOIN borrowed_books bb
                ON b.book_id = bb.book_id
            WHERE bb.student_id = ?
        """, (student_id,))

        books = self.cursor.fetchall()

        if not books:
            print("No books borrowed.")

        else:
            for book_id, title, author in books:
                print(
                    f"- ID: {book_id} | "
                    f"Title: {title} | "
                    f"Author: {author}"
                )

    # ==========================================
    # CLOSE DATABASE
    # ==========================================

    def close(self):
        self.connection.close()


# ==========================================
# MAIN PROGRAM
# ==========================================

database = Database()

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

    # ==========================================
    # ADD STUDENT
    # ==========================================

    if choice == "1":

        try:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")

            database.add_student(student_id, name)

        except ValueError:
            print("\nStudent ID must be a number.")

    # ==========================================
    # ADD BOOK
    # ==========================================

    elif choice == "2":

        try:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            database.add_book(book_id, title, author)

        except ValueError:
            print("\nBook ID must be a number.")

    # ==========================================
    # DISPLAY BOOKS
    # ==========================================

    elif choice == "3":

        database.display_books()

    # ==========================================
    # DISPLAY STUDENTS
    # ==========================================

    elif choice == "4":

        database.display_students()

    # ==========================================
    # ISSUE BOOK
    # ==========================================

    elif choice == "5":

        try:
            student_id = int(input("Enter Student ID: "))
            book_id = int(input("Enter Book ID: "))

            database.issue_book(student_id, book_id)

        except ValueError:
            print("\nIDs must be numbers.")

    # ==========================================
    # RETURN BOOK
    # ==========================================

    elif choice == "6":

        try:
            student_id = int(input("Enter Student ID: "))
            book_id = int(input("Enter Book ID: "))

            database.return_book(student_id, book_id)

        except ValueError:
            print("\nIDs must be numbers.")

    # ==========================================
    # VIEW STUDENT'S BOOKS
    # ==========================================

    elif choice == "7":

        try:
            student_id = int(input("Enter Student ID: "))

            database.view_student_books(student_id)

        except ValueError:
            print("\nStudent ID must be a number.")

    # ==========================================
    # EXIT
    # ==========================================

    elif choice == "8":

        database.close()

        print(
            "\nThank you for using the "
            "Library Management System!"
        )

        break

    else:

        print("\nInvalid choice. Please try again.")