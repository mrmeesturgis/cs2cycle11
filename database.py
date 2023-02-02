import pandas as pd
import pymysql
import re
import csv


class db():
	def __init__(self):
		self.connection=pymysql.connect(host='localhost',port=int(32000),user='root',passwd='root')
		self.cursor = self.connection.cursor()
		#self.answer = pd.read_sql_query('show databases',self.connection)
		
	def checkdb(self):
		self.answer = pd.read_sql_query('show databases',self.connection)
		print(self.answer)
		
	def builddb(self, target):
		instructions = open(target, "r")
		instructions = instructions.read()
		instructions = re.sub("\n", "", instructions)
		instructions = re.split(";", instructions)
		final = []
		for i in instructions:
			if i: final.append(i)

		for instruction in final:
			print("Sending instruction", instruction)
			self.cursor.execute(instruction)
			self.connection.commit()
			
	def checktable(self, target, table):
		result= pd.read_sql_query(f'SELECT {target} FROM {table}', self.connection)
		return result
				
		

	

#cur = conn.cursor()
#df=pd.read_sql_query('show databases',conn)


