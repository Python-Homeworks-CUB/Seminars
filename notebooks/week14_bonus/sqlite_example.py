import sqlite3


class StudentDatabase:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS students (name TEXT, grade INTEGER)"
        )
        self.conn.commit()

    def add_student(self, student, grade):
        self.cursor.execute(
            "INSERT INTO students (name, grade) VALUES (?, ?)", (student, grade)
        )
        self.conn.commit()

    def show_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close(self):
        self.conn.close()


# Usage Example
if __name__ == "__main__":
    db = StudentDatabase()

    db.create_table()
    db.add_student("Alice", 95)
    db.add_student("Bob", 88)
    print("Students:")
    db.show_students()

    db.close()
