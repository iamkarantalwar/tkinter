#insert data with variables
name = input("Enter the name")
email = input("Enter the Email")
password = input("Enter the password")
dob = input("Enter the D.O.B.")

#import the MySql Api
import mysql.connector

#create a bridge between mysql and python
#create the connection
mydb = mysql.connector.connect(
    user="root",
    passwd = "",
    host = "localhost",
    database = "first_database",
    )
#make a cursor
cursor = mydb.cursor()
cursor.execute("""INSERT INTO `users`(`name`, `email`, `password`, `dob`)
                        VALUES (%s,%s,%s,%s)""",(name,email,password,dob))
#if you use insert query then it's important to commit the command
#if you send the data from python to mysql you will use commit
mydb.commit()
