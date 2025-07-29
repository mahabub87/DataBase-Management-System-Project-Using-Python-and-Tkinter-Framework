import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

# Database Connection
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_management_system"
    )

# CRUD Functions
def add_student_to_db(student_id, name, email):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Students (student_id, name, email) VALUES (%s, %s, %s)", (student_id, name, email))
    connection.commit()
    connection.close()

def add_course_to_db(course_id, course_name, credits):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Courses (course_id, course_name, credits) VALUES (%s, %s, %s)", (course_id, course_name, credits))
    connection.commit()
    connection.close()

def assign_grade_to_db(student_id, course_id, grade):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Grades (student_id, course_id, grade) VALUES (%s, %s, %s)", (student_id, course_id, grade))
    connection.commit()
    connection.close()

def search_student_by_id(student_id):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM StudentCourseGrades WHERE student_id = %s", (student_id,))
    records = cursor.fetchall()
    connection.close()
    return records

def search_course_by_id(course_id):
    connection = connect_to_db()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CourseStudents WHERE course_id = %s", (course_id,))
    records = cursor.fetchall()
    connection.close()
    return records

# GUI Functions
def add_student():
    def save_student():
        student_id = student_id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        if student_id and name and email:
            add_student_to_db(student_id, name, email)
            messagebox.showinfo("Success", "Student added successfully!")
            student_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    student_window = tk.Toplevel(root)
    student_window.title("Add Student")
    student_window.geometry("500x350")
    student_window.configure(bg="#D3D3D3")
    
    tk.Label(student_window, text="Student ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    student_id_entry = tk.Entry(student_window, font=("Arial", 12))
    student_id_entry.pack()
    
    tk.Label(student_window, text="Name:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    name_entry = tk.Entry(student_window, font=("Arial", 12))
    name_entry.pack()
    
    tk.Label(student_window, text="Email:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    email_entry = tk.Entry(student_window, font=("Arial", 12))
    email_entry.pack()
    
    tk.Button(student_window, text="Save", command=save_student, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)

def add_course():
    def save_course():
        course_id = course_id_entry.get()
        course_name = course_name_entry.get()
        credits = credits_entry.get()
        if course_id and course_name and credits.isdigit():
            add_course_to_db(course_id, course_name, int(credits))
            messagebox.showinfo("Success", "Course added successfully!")
            course_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required and Credits must be a number!")

    course_window = tk.Toplevel(root)
    course_window.title("Add Course")
    course_window.geometry("500x350")
    course_window.configure(bg="#D3D3D3")
    
    tk.Label(course_window, text="Course ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_id_entry = tk.Entry(course_window, font=("Arial", 12))
    course_id_entry.pack()
    
    tk.Label(course_window, text="Course Name:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_name_entry = tk.Entry(course_window, font=("Arial", 12))
    course_name_entry.pack()
    
    tk.Label(course_window, text="Credits:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    credits_entry = tk.Entry(course_window, font=("Arial", 12))
    credits_entry.pack()
    
    tk.Button(course_window, text="Save", command=save_course, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)

def assign_grade():
    def save_grade():
        student_id = student_id_entry.get()
        course_id = course_id_entry.get()
        grade = grade_entry.get()
        if student_id and course_id and grade:
            assign_grade_to_db(student_id, course_id, grade)
            messagebox.showinfo("Success", "Grade assigned successfully!")
            grade_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    grade_window = tk.Toplevel(root)
    grade_window.title("Assign Grade")
    grade_window.geometry("500x350")
    grade_window.configure(bg="#D3D3D3")
    
    tk.Label(grade_window, text="Student ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    student_id_entry = tk.Entry(grade_window, font=("Arial", 12))
    student_id_entry.pack()
    
    tk.Label(grade_window, text="Course ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_id_entry = tk.Entry(grade_window, font=("Arial", 12))
    course_id_entry.pack()
    
    tk.Label(grade_window, text="Grade:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    grade_entry = tk.Entry(grade_window, font=("Arial", 12))
    grade_entry.pack()
    
    tk.Button(grade_window, text="Save", command=save_grade, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)

def update_student_in_db(student_id, name, email):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.callproc('UpdateStudent', [student_id, name, email])
    connection.commit()
    connection.close()

def update_course_in_db(course_id, course_name, credits):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.callproc('UpdateCourse', [course_id, course_name, credits])
    connection.commit()
    connection.close()

def update_grade_in_db(student_id, course_id, grade):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.callproc('UpdateGrade', [student_id, course_id, grade])
    connection.commit()
    connection.close()

# GUI Functions
def update_student():
    def save_update_student():
        student_id = student_id_entry.get()
        name = name_entry.get()
        email = email_entry.get()
        if student_id and name and email:
            update_student_in_db(student_id, name, email)
            messagebox.showinfo("Success", "Student updated successfully!")
            update_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    update_window = tk.Toplevel(root)
    update_window.title("Update Student")
    update_window.geometry("500x350")
    update_window.configure(bg="#D3D3D3")
    
    tk.Label(update_window, text="Student ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    student_id_entry = tk.Entry(update_window, font=("Arial", 12))
    student_id_entry.pack()
    
    tk.Label(update_window, text="Name:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    name_entry = tk.Entry(update_window, font=("Arial", 12))
    name_entry.pack()
    
    tk.Label(update_window, text="Email:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    email_entry = tk.Entry(update_window, font=("Arial", 12))
    email_entry.pack()
    
    tk.Button(update_window, text="Save", command=save_update_student, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)

def update_course():
    def save_update_course():
        course_id = course_id_entry.get()
        course_name = course_name_entry.get()
        credits = credits_entry.get()
        if course_id and course_name and credits.isdigit():
            update_course_in_db(course_id, course_name, int(credits))
            messagebox.showinfo("Success", "Course updated successfully!")
            update_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required and Credits must be a number!")

    update_window = tk.Toplevel(root)
    update_window.title("Update Course")
    update_window.geometry("500x350")
    update_window.configure(bg="#D3D3D3")
    
    tk.Label(update_window, text="Course ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_id_entry = tk.Entry(update_window, font=("Arial", 12))
    course_id_entry.pack()
    
    tk.Label(update_window, text="Course Name:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_name_entry = tk.Entry(update_window, font=("Arial", 12))
    course_name_entry.pack()
    
    tk.Label(update_window, text="Credits:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    credits_entry = tk.Entry(update_window, font=("Arial", 12))
    credits_entry.pack()
    
    tk.Button(update_window, text="Save", command=save_update_course, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)

def update_grade():
    def save_update_grade():
        student_id = student_id_entry.get()
        course_id = course_id_entry.get()
        grade = grade_entry.get()
        
        # Ensure all fields are filled
        if student_id and course_id and grade:
            try:
                # Call stored procedure to update grade
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.callproc('UpdateGrade', (student_id, course_id, grade))
                conn.commit()
                messagebox.showinfo("Success", "Grade updated successfully!")
                update_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
        else:
            messagebox.showerror("Error", "All fields are required!")

    # Create the update grade window
    update_window = tk.Toplevel(root)
    update_window.title("Update Grade")
    update_window.geometry("400x300")
    update_window.configure(bg="#D3D3D3")

    # Labels and entry fields
    tk.Label(update_window, text="Student ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    student_id_entry = tk.Entry(update_window, font=("Arial", 12))
    student_id_entry.pack()

    tk.Label(update_window, text="Course ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_id_entry = tk.Entry(update_window, font=("Arial", 12))
    course_id_entry.pack()

    tk.Label(update_window, text="Grade:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    grade_entry = tk.Entry(update_window, font=("Arial", 12))
    grade_entry.pack()

    # Save button
    tk.Button(update_window, text="Save", command=save_update_grade, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=20)


    
    
def view_student_details():
    def search_student():
        student_id = student_id_entry.get()
        if student_id:
            try:
                records = search_student_by_id(student_id)
                # Clear the treeview before inserting new data
                for row in tree.get_children():
                    tree.delete(row)
                # Insert data into the treeview
                for record in records:
                    tree.insert(
                        "", 
                        "end", 
                        values=(
                            record.get('student_id', 'N/A'), 
                            record.get('name', 'N/A'), 
                            record.get('email', 'N/A'), 
                            record.get('course_name', 'N/A'), 
                            record.get('grade', 'N/A')
                        )
                    )
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Input Required", "Please enter a Student ID to search.")

    # Create a new window for viewing student details
    view_window = tk.Toplevel(root)
    view_window.title("Student Details")
    view_window.geometry("800x500")
    view_window.configure(bg="#D3D3D3")

    # Input field for Student ID
    tk.Label(view_window, text="Enter Student ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    student_id_entry = tk.Entry(view_window, font=("Arial", 12))
    student_id_entry.pack()

    # Search button
    tk.Button(view_window, text="Search", command=search_student, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=10)

    # Define columns for the Treeview
    columns = ("Student ID", "Name", "Email", "Course", "Grade")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill="both", expand=True)


def view_course_details():
    def search_course():
        course_id = course_id_entry.get()
        if course_id:
            records = search_course_by_id(course_id)
            for row in tree.get_children():
                tree.delete(row)
            for record in records:
                tree.insert("", "end", values=(record['course_id'], record['course_name'], record['student_id'], record['name'], record['grade']))

    view_window = tk.Toplevel(root)
    view_window.title("Course Details")
    view_window.geometry("800x500")
    view_window.configure(bg="#D3D3D3")

    tk.Label(view_window, text="Enter Course ID:", bg="#D3D3D3", font=("Arial", 12)).pack(pady=10)
    course_id_entry = tk.Entry(view_window, font=("Arial", 12))
    course_id_entry.pack()

    tk.Button(view_window, text="Search", command=search_course, bg="#008080", fg="white", font=("Arial", 12)).pack(pady=10)

    columns = ("Course ID", "Course Name", "Student ID", "Name", "Grade")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)
    tree.pack(fill="both", expand=True)

def exit_program():
    root.quit()
    
# Function to open Update Interface
def open_update_interface():
    update_window = tk.Toplevel(root)
    update_window.title("Update Options")
    update_window.geometry("400x300")
    update_window.configure(bg="#FFD700")

    tk.Label(update_window, text="Update Options", bg="#FFD700", font=("Arial Bold", 16)).pack(pady=20)
    
    tk.Button(update_window, text="Update Student", command=update_student, bg="#F0E68C", font=("Arial", 12), width=20).pack(pady=10)
    tk.Button(update_window, text="Update Course", command=update_course, bg="#F0E68C", font=("Arial", 12), width=20).pack(pady=10)
    tk.Button(update_window, text="Update Grade", command=update_grade, bg="#F0E68C", font=("Arial", 12), width=20).pack(pady=10)

# Function to open View Interface
def open_view_interface():
    view_window = tk.Toplevel(root)
    view_window.title("View Options")
    view_window.geometry("400x300")
    view_window.configure(bg="#0074D9")

    tk.Label(view_window, text="View Options", bg="#0074D9", fg="white", font=("Arial Bold", 16)).pack(pady=20)
    
    tk.Button(view_window, text="View Student Details", command=view_student_details, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)
    tk.Button(view_window, text="View Course Details", command=view_course_details, bg="#4682B4", fg="white", font=("Arial", 12), width=20).pack(pady=10)

# Main GUI
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x700")
root.configure(bg="#003366")

tk.Label(root, text="Student Management System", bg="#003366", fg="white", font=("Arial Bold", 20)).pack(pady=20)

tk.Button(root, text="Add Student", command=add_student, bg="#008080", fg="white", font=("Arial", 14), width=20).pack(pady=10)
tk.Button(root, text="Add Course", command=add_course, bg="#008080", fg="white", font=("Arial", 14), width=20).pack(pady=10)
tk.Button(root, text="Assign Grade", command=assign_grade, bg="#008080", fg="white", font=("Arial", 14), width=20).pack(pady=10)

# Update Button to open Update Interface
tk.Button(root, text="Update", command=open_update_interface, bg="#FFD700", fg="black", font=("Arial", 14), width=20).pack(pady=10)

# View Button to open View Interface
tk.Button(root, text="View", command=open_view_interface, bg="#0074D9", fg="white", font=("Arial", 14), width=20).pack(pady=10)

tk.Button(root, text="Exit", command=exit_program, bg="#FF5733", fg="white", font=("Arial", 14), width=20).pack(pady=20)

root.mainloop()






# Query 
'''CREATE DATABASE IF NOT EXISTS student_management_system;
USE student_management_system;

-- Create Tables
CREATE TABLE IF NOT EXISTS Students (
    student_id VARCHAR(10) PRIMARY KEY UNIQUE,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Courses (
    course_id VARCHAR(10) PRIMARY KEY UNIQUE,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id VARCHAR(10),
    course_id VARCHAR(10),
    grade VARCHAR(5),
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE
);

-- Create Views
CREATE OR REPLACE VIEW StudentCourseGrades AS
SELECT 
    s.student_id, 
    s.name, 
    c.course_id, 
    c.course_name, 
    g.grade
FROM Students s
LEFT JOIN Grades g ON s.student_id = g.student_id
LEFT JOIN Courses c ON g.course_id = c.course_id;

CREATE OR REPLACE VIEW CourseStudents AS
SELECT 
    c.course_id, 
    c.course_name, 
    s.student_id, 
    s.name, 
    g.grade
FROM Courses c
LEFT JOIN Grades g ON c.course_id = g.course_id
LEFT JOIN Students s ON g.student_id = s.student_id;

-- Stored Procedures
DELIMITER $$

-- Update Student Procedure
CREATE OR REPLACE PROCEDURE UpdateStudent(
    IN p_student_id VARCHAR(10),
    IN p_name VARCHAR(100),
    IN p_email VARCHAR(100)
)
BEGIN
    UPDATE Students
    SET name = p_name, email = p_email
    WHERE student_id = p_student_id;
END$$

-- Update Course Procedure
CREATE OR REPLACE PROCEDURE UpdateCourse(
    IN p_course_id VARCHAR(10),
    IN p_course_name VARCHAR(100),
    IN p_credits INT
)
BEGIN
    UPDATE Courses
    SET course_name = p_course_name, credits = p_credits
    WHERE course_id = p_course_id;
END$$

-- Update Grade Procedure
CREATE OR REPLACE PROCEDURE UpdateGrade(
    IN p_student_id VARCHAR(10),
    IN p_course_id VARCHAR(10),
    IN p_grade VARCHAR(5)
)
BEGIN
    UPDATE Grades
    SET grade = p_grade
    WHERE student_id = p_student_id AND course_id = p_course_id;
END$$

DELIMITER ;'''