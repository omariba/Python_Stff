import MySQLdb

con = MySQLdb.connect("localhost","root","toor","pyclass")

place = con.cursor()
query = "insert into students(`Admin No`,Fname,Lname)values(1,'Genius','Persons');"
place.execute(query)
con.commit()

con.close()