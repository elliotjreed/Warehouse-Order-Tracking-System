#!/usr/bin/python3
#Note: Indented using tabs (ie. not spaces..duh!)
import time
import mysql.connector
import re

loop = 1
while loop == 1:
	try:
		db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
		cur = db.cursor()

		order = input('Order ID or Postcode: ')
		match = re.search(r'^[a-zA-Z][a-zA-Z][0-9]+[a-zA-Z][a-zA-Z]+', order) # matches postcodes too :(

		if match:
			print('Please scan the Order ID first, then the Tracking Number - start again!')
			order = input('Order ID or Postcode: ')

		track = input('Tracking Number: ')
		match = re.search(r'^[a-zA-Z][a-zA-Z][0-9]+[a-zA-Z][a-zA-Z]+', track)

		if match:
			thetime = time.strftime('%H:%M:%S')
			thedate = time.strftime('%Y-%m-%d')
			cur.execute('INSERT INTO first_class (orderid,tracking,date,time) VALUES (%s,%s,%s,%s)',(order, track, thedate, thetime))
			db.commit()

		else:
			print('Please scan the Order ID first, then the Tracking Number - start again!')

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with the database username and password, which isn't good - tell Elliot if it doesn't start working in the next 2 minutes..")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist, please tell Elliot if it doesn't start working in the next 2 minutes..")
		else:
			print(err)
			print("Something's not working properly, please tell Elliot if it doesn't start working in the next 2 minutes..")
			time.sleep(10)
	else:
		db.close()


cur.close()
db.close()
