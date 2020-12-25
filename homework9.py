import json
import csv
import time 
import datetime


registered_at = time.ctime(time.time())
time = datetime.datetime.now() 


myData_csv = {{"id","username","email","ip_address", "time", "registered_at"},
			{'1','admin','admin@example.com','192.168.0.1', time, registered_at}, 
			{'2','test_user','test_user@example.com','192.168.0.2', time, registered_at},
			{'3','second_user','second_user@example.com','192.168.0.3', time, registered_at}}

'''
data_json = {
	"username": "admin",
	"email": "admin@example.com",
	"ip_address": "192.168.0.1",
	"time": time	
}
'''
myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.csv', 'w')
with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData_csv)

myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.csv')
with myFile:
print(myFile.load())
print('Записи записаны в формате csv') 

'''
with open("C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.json", "w") as file:
	json.dump(data_json, file)

with open("C:\\Users\\Home\\Desktop\\python\\Урок9\\homework9_data.json") as file:
	print(json.load(file))
print('Записи записаны в формате json') 
'''