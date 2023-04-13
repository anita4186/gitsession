import mysql.connector

def get_mysql_data():
	try:
		dataBase = mysql.connector.connect(host ="localhost", user ="root", password ="root", database = "project2")
		 
		#preparing a cursor object
		cursorObject = dataBase.cursor()
		  
		query = "SELECT * FROM retailbase"
		cursorObject.execute(query)

		myresult = cursorObject.fetchall()
		
		return myresult
	
	except:
	
		print("some issue in connection")
def get_mysql_data1():
        try:
                dataBase = mysql.connector.connect(host ="localhost", user ="root", password ="root", database = "project2")

                #preparing a cursor object
                cursorObject = dataBase.cursor()

                query = "SELECT * FROM retailnew"
                cursorObject.execute(query)

                myresult = cursorObject.fetchall()

                return myresult

        except:

                print("some issue in connection")

		

print(get_mysql_data())
print("pulled the1st table successfully.......!")
print(get_mysql_data1())
print("pulled 2nd table successfully.......!")

