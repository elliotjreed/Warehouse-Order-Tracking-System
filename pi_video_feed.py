#!/usr/bin/python3
#Note: Indented using tabs
# sudo aptitude update && sudo aptitude -r full-upgrade -y && sudo -r aptitude install python3-setuptools && sudo easy_install3 picamera mysql-connector-python -y
import time
import mysql.connector
from mysql.connector import errorcode
import picamera
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
loop1 = 1
while loop1 == 1:
	try:
		db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
		cur = db.cursor()
		loop2 = 1
		empid = input('Employee ID: ')
		order = input('Order ID or Staff ID: ')
		while loop2 == 1:
			if 'emp' in order:
				empid = order
				order = input('Order ID: ')
			thetime = time.strftime('%H:%M:%S')
			thedate = time.strftime('%Y-%m-%d')
			cur.execute('INSERT INTO packed (orderid,employee_id,date,time) VALUES (%s,%s,%s,%s)',(order, empid, thedate, thetime))
			db.commit()
			savefile = '/home/pi/Orders/[{0}]{1}_{2}_{3}.h264'.format(order, empid, thedate, thetime)
			with picamera.PiCamera() as camera:
				camera.resolution = (1280, 720)
				camera.start_recording('{0}'.format(savefile))
				order = input('Order ID or Staff ID: ')
				camera.stop_recording()
		camera.close()
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
				time.sleep(5)
				continue
			else:
				print('Not connected to the internet! Waiting for 10 seconds before trying again..')
				time.sleep(10)
				continue
	else:
		db.close()
