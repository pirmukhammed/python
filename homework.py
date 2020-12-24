'''homework8'''
import csv

myData = [["id","username","email","ip_address"],
			['1','admin','admin@example.com','192.168.0.1'], 
			['2','test_user','test_user@example.com','192.168.0.2'],
			['3','second_user','second_user@example.com','192.168.0.3']]
'''Вариант с местом указания файла'''
myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок8\\data.csv', 'w')

'''Вариант файла с кодами'''
myFile = open('data.csv', 'w')
with myFile:
		writer = csv.writer(myFile)
		writer.writerows(myData)

myFile = open('C:\\Users\\Home\\Desktop\\python\\Урок8\\data.csv', 'r')
print(myFile.read())
print('Записи записаны') 
