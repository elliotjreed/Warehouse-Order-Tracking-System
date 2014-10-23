#!/usr/bin/python3
import time
import mysql.connector
import pyaudio
import wave
class AudioFile:
	chunk = 1024
	def __init__(self, file):
		self.wf = wave.open(file, 'rb')
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(
			format = self.p.get_format_from_width(self.wf.getsampwidth()),
			channels = self.wf.getnchannels(),
			rate = self.wf.getframerate(),
			output = True
		)
	def play(self):
		data = self.wf.readframes(self.chunk)
		while data != '':
			self.stream.write(data)
			data = self.wf.readframes(self.chunk)
	def close(self):
		self.stream.close()
		self.p.terminate()

#time.sleep(5)

def internet_on():
	try:
		response=urllib3.urlopen('http://173.194.41.175',timeout=1)
		return True
	except urllib3.URLError as err: pass
	return False
if internet_on:
	print('Enter or Scan the Tracking Number')
else:
	print('No net con. Wait 10.')
	time.sleep(10)
db = mysql.connector.connect(host='IPOFDATABASESERVER', user='DATABASEUSERNAME', passwd='DATABASEPASSWORD', db='DATABASENAME')
cur = db.cursor()
loop = 1
while loop == 1:
	try:
		bar = input()
		if 'JJD' in bar:
			thetime = time.strftime('%H:%M:%S')
			thedate = time.strftime('%Y-%m-%d')
			cur.execute("SELECT tracking FROM yodel WHERE tracking='" + bar + "'")
			check = cur.fetchone()
			if check == None:
				cur.execute('INSERT INTO yodel (tracking,date,time) VALUES (%s,%s,%s)',(bar, thedate, thetime))
				db.commit()
			else:
				a = AudioFile('scream.wav')
				a.play()
				a.close()
		else:
			a = AudioFile('alarm.wav')
			a.play()
			a.close()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			time.sleep(5)
			continue
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			time.sleep(5)
			continue
		else:
			print(err)
			if internet_on:
				continue
			else:
				time.sleep(10)
				continue
	else:
		time.sleep(5)
		continue
cur.close()
db.close()
