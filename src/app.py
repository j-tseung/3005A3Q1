# /src/app.py
import psycopg2
from db import connect_db

def getAllStudents():
    """Retrieves and displays all student records from the students table in a formatted table."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students ORDER BY student_id ASC")
        students = cursor.fetchall()
        
        # Print header
        print(f"{'Student ID':<10} {'First Name':<15} {'Last Name':<15} {'Email':<40} {'Enrollment Date':<15}")
        print('-' * 100)  
        
        # Print each student's details in a formatted way
        for student in students:
            print(f"{student['student_id']:<10} {student['first_name']:<15} {student['last_name']:<15} {student['email']:<40} {student['enrollment_date']}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the students table."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def updateStudentEmail(student_id, new_email):
    """Updates the email address for a student with the specified student_id."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        conn.commit()
        print("Email updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()

def deleteStudent(student_id):
    """Deletes the record of the student with the specified student_id."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        print("Student deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()
        
def main():
    while True:
        print("\nStudent Management System")
        print("1. List all students")
        print("2. Add a new student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            getAllStudents()
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            new_email = input("Enter new email: ")
            updateStudentEmail(student_id, new_email)
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            deleteStudent(student_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
