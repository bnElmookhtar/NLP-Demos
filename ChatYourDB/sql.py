import sqlite3


connection = sqlite3.connect('students.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
name varchar(10),
class varchar(10),
marks int
)
''')

cursor.execute('''
INSERT INTO students (name, class, marks) VALUES
('Alice', '10A', 85),
('Bob', '10B', 90),
('Charlie', '10A', 78)
''')

print(cursor.execute('SELECT * FROM students').fetchall())
connection.commit()
connection.close()
