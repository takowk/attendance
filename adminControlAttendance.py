import mysql.connector
from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="attendance"
)

reader = SimpleMFRC522()
mycursor = mydb.cursor()
table = "attendance"

def addStudent(mycursor, table):
    print("ADD STUDENT\nPlace your tag to read...")
    id,text = reader.read()
    classid = input("Enter classID: ")
    sql = "INSERT INTO " + table + " (studentid, classid, datetime) VALUES (%s, %s, %s)"
    val = (id,classid,str(datetime.now()))
    print(sql,val)
    mycursor.execute(sql, val)
    mydb.commit()
    print("inserted.")
    
def showData(mycursor, table):
    mycursor.execute("SELECT * FROM " + table)
    myresult = mycursor.fetchall()
    print("\ntable contents:")
    for x in myresult:
        print(x)
        
def removeAttendance(mycursor, table):
    print("REMOVE ATTENDANCE\nPlace your tag to read...")
    id, text = reader.read()
    sql = "DELETE FROM `"+ table +"` WHERE studentid = '" + str(id) + "';"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print("removed.")
    
def updateTable(mycursor, table):
    print("UPDATING ATTENDANCE\nPlace your tag to read...")
    id, text = reader.read()
    classid = input("Enter classID: ")
    sql = "UPDATE `" + table + "` SET `classid` = '" + classid + "' WHERE studentid = '" + str(id) + "';"
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print("updated.")
    

#addStudent(mycursor, table)
#removeAttendance(mycursor, table)
#updateTable(mycursor, table)
#showData(mycursor, table)