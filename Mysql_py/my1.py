import MySQLdb as mysql

conn = mysql.connect('localhost','root','','pyprac')

edit = conn.cursor()

query = "insert into users(ID,First_Name,Last_Name,Phone_NO)values('','Michaels1','Jordans','0715157560')"

edit.execute(query)

read = edit.fetchone()

print read

conn.commit()
conn.close()
