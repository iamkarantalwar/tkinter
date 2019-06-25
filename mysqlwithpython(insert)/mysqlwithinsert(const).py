#program to insert the data into databse with constant values
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
#insert query
cursor.execute("INSERT INTO `users`( `name`, `email`, `password`, `dob`) VALUES ('Karan','karan@o7services.com','o7services','1-12-1994')")
#if you use insert query then it's important to commit the command
#if you send the data from python to mysql you will use commit
mydb.commit()

