import MySQLdb as mysql

connection = mysql.connect('localhost','root','','pyprac')
nav = connection.cursor()
query = 'create table `mandela1`(fname varchar(30),lname varchar(30));'
query1 = 'select * from users'
query2 = 'show tables in pyprac'

#nav.execute(query1)
nav.execute(query2)
me = nav.fetchall()
#one = nav.fetchone()

#for one in me:
#	print one

#f = list(me)
#print f[1][1]

#print me[0][2]

#for us in me:
#	print us[0],".",us[1], "|",us[2],"|", us[3]

for tab in me:
	print tab[0]
connection.commit()
connection.close()
