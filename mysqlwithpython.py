#import mysql API
import mysql.connector
#make a bridge between python and mysql
#make a connection
mydb = mysql.connector.connect(
    user="localhost",
    passwd="",
    host="localhost",
    database="database_name")

#make a cursor to communicate with mysql and python
#mycursor will act as a car
mycursor = mydb.cursor()
#how to get data in the car of table.
mycursor.execute("SELECT * FROM `table_name`")

#load the data from the car to your bag
#data will act as a bag
data = mycursor.fetchall()
