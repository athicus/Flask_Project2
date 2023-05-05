import mysql.connector as sql
conn = sql.connect(host="localhost",	user="flask",	password="ubuntu",	database="flask_db")
cur = conn.cursor()
cmd = "CREATE TABLE employees (\
	EmpID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
	EmpName	VARCHAR(30) NOT	NULL, \
	EmpGender CHAR(1), \
	EmpPhone VARCHAR(15), \
	EmpBdate VARCHAR(30))"
cur.execute(cmd)
conn.close()
