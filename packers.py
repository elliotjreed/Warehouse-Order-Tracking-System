#!/usr/bin/python3
import time
import colorama
from colorama import Fore, Back, Style
import mysql.connector
from mysql.connector import errorcode
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
loop = 1
while loop == 1:
	try:
		db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
		cur = db.cursor()
		colorama.init()
		bartext = 'Scan the Staff ID '
		ordertext = 'Scan the Order ID '
		text = 'Scan the Order ID or Staff ID '
		bar = input(Back.RED + bartext + Style.RESET_ALL)
		order = input(Back.GREEN + ordertext + Style.RESET_ALL)
		while 'emp' in bar:
			thetime = time.strftime('%H:%M:%S')
			thedate = time.strftime('%Y-%m-%d')
			cur.execute('INSERT INTO pack (orderid,employee_id,time,date) VALUES (%s,%s,%s,%s)',(order, bar, thetime, thedate))
			db.commit()
			order = input(Back.GREEN + text + Style.RESET_ALL)
			if 'emp' in order:
				bar = order
				order = input(Back.GREEN + ordertext + Style.RESET_ALL)
		cur.close()
		db.close()
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
				print('The device is connected to the internet, it may have been a temporary loss of connection or a duplicate entry. Try scanning again..')
				continue
			else:
				print('Not connected to the internet! Waiting for 10 seconds before trying again..')
				cur.close()
				db.close()
				time.sleep(10)
				continue
	else:
		db.close()
