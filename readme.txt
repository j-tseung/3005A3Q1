Jearina Tseung
101199241
COMP3005 A3Q1

Project Directory Structure
/project-root
    /database
        - setup.sql         # Script for creating the database and inserting initial data
    /src
        - app.py            # Main application file with CRUD functions
        - db.py             # Database connection utility
    /README.md              # Instructions on setup and how to run the application

# Student Management Application

## Introduction
This application connects to a PostgreSQL database to perform CRUD operations on a `students` table, allowing for the management of student records.

## Setup
1. Download 3005A3Q1-main.
2. Extract files. 
3. Ensure PostgreSQL is installed and running on your machine.
4. Create a database and execute the `setup.sql` script to create the `students` table and insert initial data.

## Running the Application
1. Install `psycopg2` using pip: `pip install psycopg2`.
2. In /src, run `app.py` using Python: `python app.py`.
3. Use the menu options to interact with the database.

## Function Descriptions
- `getAllStudents()`: Displays all student records.
- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record.
- `updateStudentEmail(student_id, new_email)`: Updates a student's email.
- `deleteStudent(student_id)`: Deletes a student's record.

## Demonstration Video
https://youtu.be/1futAqOuDGc
