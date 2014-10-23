#!/usr/bin/python3
#Note: Indented using tabs (ie. not spaces..duh!)
import time
import mysql.connector

db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
cur = db.cursor()
loop = 1

while loop == 1:
	bar = input('Order ID: ')
	cur.execute('SELECT orderid FROM second_class WHERE orderid= ' + bar + ';')
	check = cur.fetchone()
	if check == None:
		thetime = time.strftime('%H:%M:%S')
		thedate = time.strftime('%Y-%m-%d')
		cur.execute('INSERT INTO second_class (orderid,date,time) VALUES (%s,%s,%s)',(bar, thedate, thetime))
		db.commit()
	else:
		print("This order has already been scanned, although it's very commendable that you want to do more work..")

cur.close()
db.close()
