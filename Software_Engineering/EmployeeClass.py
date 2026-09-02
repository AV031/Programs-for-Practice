import sqlite3
import pandas as pd

DB_NAME = "employee_storage.db"


# ---------------- DATABASE ----------------

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            empid INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            dept TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- EMPLOYEE CLASS ----------------

class Emp:

    def __init__(self):
        self.__empid = 0
        self.__name = ""
        self.__dept = ""
        self.__salary = 0.0

    # Get Salary
    def get_salary(self, empid):

        conn = sqlite3.connect(DB_NAME)

        query = "SELECT salary FROM employees WHERE empid = ?"

        result = pd.read_sql_query(
            query,
            conn,
            params=(empid,)
        )

        conn.close()

        if not result.empty:
            return result.iloc[0]["salary"]

        return None

    # Get Department
    def get_dept(self, empid):

        conn = sqlite3.connect(DB_NAME)

        query = "SELECT dept FROM employees WHERE empid = ?"

        result = pd.read_sql_query(
            query,
            conn,
            params=(empid,)
        )

        conn.close()

        if not result.empty:
            return result.iloc[0]["dept"]

        return None

    # Store Employee
    def _store(self, empid, name, dept, salary):

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT OR REPLACE INTO employees
            (empid, name, dept, salary)
            VALUES (?, ?, ?, ?)
        """, (empid, name, dept, salary))

        conn.commit()
        conn.close()


# ---------------- DISPLAY TABLE ----------------

def show_table():

    conn = sqlite3.connect(DB_NAME)

    df = pd.read_sql_query(
        "SELECT * FROM employees ORDER BY empid",
        conn
    )

    conn.close()

    if df.empty:
        print("\nNo employee records found.")

    else:
        print("\n========== EMPLOYEE TABLE ==========")
        print(df.to_string(index=False))


# ---------------- DELETE EMPLOYEE ----------------

def delete_employee(empid):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM employees WHERE empid = ?",
        (empid,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee ID not found.")

    conn.close()


# ---------------- MAIN PROGRAM ----------------

create_database()

employee = Emp()

while True:

    print("\n======================================")
    print("      EMPLOYEE MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add / Update Employee")
    print("2. Get Salary")
    print("3. Get Department")
    print("4. Show Employee Table")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # Add employee
    if choice == "1":

        empid = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        dept = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee._store(
            empid,
            name,
            dept,
            salary
        )

        print("Employee stored successfully.")

    # Get salary
    elif choice == "2":

        empid = int(input("Enter Employee ID: "))

        salary = employee.get_salary(empid)

        if salary is not None:
            print("Salary:", salary)
        else:
            print("Employee ID not found.")

    # Get department
    elif choice == "3":

        empid = int(input("Enter Employee ID: "))

        dept = employee.get_dept(empid)

        if dept is not None:
            print("Department:", dept)
        else:
            print("Employee ID not found.")

    # Display table
    elif choice == "4":

        show_table()

    # Delete employee
    elif choice == "5":

        empid = int(input("Enter Employee ID: "))

        delete_employee(empid)

    # Exit
    elif choice == "6":

        print("Program closed.")
        break

    else:

        print("Invalid choice. Please try again.")