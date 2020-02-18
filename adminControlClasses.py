import mysql.connector
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
#from gpiozero import Button
lcd = CharLCD('PCF8574', 0X27)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="attendance"
)

reader = SimpleMFRC522()
mycursor = mydb.cursor()
table = "classes_club"

#button = Button(26)

def addClassClub(mycursor, table):
    name = input("Name of class or club:")
    teacher = input("Name of the teacher:")
    sql = "INSERT INTO " + table + " (name, teacher) VALUES (%s, %s)"
    val = (name, teacher)
    mycursor.execute(sql, val)
    mydb.commit()
    print("inserted.")
    
def removeClassClub(mycursor, table):
    name = input("What class/club do you want to remove? ")
    sql = "DELETE FROM `"+ table +"` WHERE name = '" + name + "';"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print("removed.")
    
def showData(mycursor, table):
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()
    print("\ntable contents:")
    for x in myresult:
        print(x)
    
def dropTable(mycursor, table):
    sql = "DROP TABLE " + table
    mycursor.execute(sql)
    mydb.commit()
    
def updateTable(mycursor, table):
    showData(mycursor, table)
    name = input("What class do you want to update the teacher's name?: ")
    newTeacher = input("Enter new teacher's name: ")
    sql = "UPDATE `" + table + "` SET `teacher` = '" + newTeacher + "' WHERE name = '" + name + "';"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print("updated.")

#removeClassClub(mycursor, table)
#addClassClub(mycursor, table)
#updateTable(mycursor, table)

#showData(mycursor, table)
