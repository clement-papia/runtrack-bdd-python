import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="LaPlateforme"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

for student in students:
    print(student)
