import sqlite3
def connect_database():
    connection = sqlite3.connect("students.db")
    return connection 
def create_table():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS students (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL UNIQUE,
       average REAL NOT NULL
)
""")
    connection.commit()
    connection.close()
def add_student(name,average):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
            "INSERT  OR REPLACE INTO students (name,average) VALUES (?,?)",
            (name,average)
        )
    connection.commit()
    connection.close()
def get_all_students():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    connection.close()
    return students
def delete_student(name):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        "DELETE FROM students WHERE name = ?",
        (name,)
    )
    deleted = cursor.rowcount
    connection.commit()
    connection.close()
    return deleted
def update_student(name, new_average):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET average = ? WHERE name = ?",
        (new_average, name)
    )

    updated = cursor.rowcount

    connection.commit()
    connection.close()

    return updated
def find_student(name):
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )
    student = cursor.fetchone()
    connection.close()
    return student