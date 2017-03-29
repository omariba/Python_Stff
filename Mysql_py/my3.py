import MySQLdb

choice = 0
while choice != 1 and choice !=2:
	choice = input("Type 1 to read from database\nType 2 to insert into database\n")
	con = MySQLdb.connect("localhost","root","toor","pyclass")

	place = con.cursor()

	if choice == 1:
		query = "select * from students"
		place.execute(query)
		data = place.fetchall()
		for y in data:
			print y
		con.close()
	elif choice == 2:
		# query = "insert into students(`Admin No`,Fname,Lname)values(1,'Genius','Persons');"
		query = raw_input("enter your query here: ")
		place.execute(query)
		con.commit()
		con.close()
	else:
		print "INVALID CHOICE"
		con.close()
