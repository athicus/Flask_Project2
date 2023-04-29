import sqlite3 as sql
conn = sqlite3.connect('database.db')
print("Opened	database	successfully")
conn.execute('CREATE TABLE students (EmpID Text, EmpName	TEXT,	EmpGender	TEXT,	EmpPhone TEXT,	EmpBdate	TEXT)')
print("Table created	successfully")
conn.close()
