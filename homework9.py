import csv
import time 
import datetime


registered_at = time.ctime(time.time())
time = datetime.datetime.now() 

myData = [["id","username","email","ip_address", "time", "registered_at", ],
			['1','admin','admin@example.com','192.168.0.1', time, registered_at], 
			['2','test_user','test_user@example.com','192.168.0.2', time, registered_at],
			['3','second_user','second_user@example.com','192.168.0.3', time, registered_at]]

myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.csv', 'w')
with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)

myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.csv', 'r')
print(myFile.read())
print('Записи записаны') 