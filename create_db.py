import sqlite3 as sql
conn = sql.connect('database.db')
print("Opened	database	successfully")
conn.execute('CREATE TABLE employees (EmpID Text, EmpName	TEXT,	EmpGender	TEXT,	EmpPhone TEXT,	EmpBdate	TEXT)')
print("Table created	successfully")
conn.close()
