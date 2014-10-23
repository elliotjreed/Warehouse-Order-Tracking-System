#!/usr/bin/python3
#Note: Indented using tabs (ie. not spaces..duh!)
import time
import mysql.connector
db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
cur = db.cursor()
loop = 1

def internet_on():
	try:
		response=urllib3.urlopen('http://173.194.41.175',timeout=1)
		return True
	except urllib3.URLError as err: pass
	return False
if internet_on:
	print('Ready to start! Have fun..')
else:
	print('Not connected to the internet yet! Please wait a few seconds..')
	time.sleep(5)

while loop == 1:
	try:
		bar = input('Scan the Staff ID: ')
		order = input('Scan the Order ID: ')

		while 'emp' in bar:
			thetime = time.strftime('%H:%M:%S')
			thedate = time.strftime('%Y-%m-%d')
			cur.execute('SELECT orderid FROM pick WHERE orderid= ' + order + ';')
			check = cur.fetchone()

			if check == None:
				cur.execute('INSERT INTO pick (orderid,employee_id,time,date) VALUES (%s,%s,%s,%s)',(order, bar, thetime, thedate))
				db.commit()

			else:
				print('Warning! This has been scanned before - please give the order to Anna or Davison.')

			order = input('Scan the Order ID or Staff ID: ')

			if 'emp' in order:
				bar = order
				order = input('Scan the Order ID: ')

	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is (apparently..) wrong with the database username and password, which isn't good - tell Elliot if it doesn't start working in the next 2 minutes..")
			time.sleep(5)
			continue
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database supposedly does not exist, please tell Elliot if it doesn't start working in the next 2 minutes..")
			time.sleep(5)
			continue
		else:
			print(err)
			if internet_on:
				print('The device is connected to the internet, it may have been a temporary loss of connection. Try scanning again..')
				continue
			else:
				print('Not connected to the internet! Waiting for 10 seconds before trying again..')
				time.sleep(10)
				continue
	else:
		db.close()

cur.close()
db.close()
