from pymongo import MongoClient
import csv



def connection():
    # 1:Connect Mongo Client 
    conn=MongoClient('mongodb://localhost:27017/')
    # 2:Connect database
    db=conn.final_project
    # dblist = db.list_database_names()
    # if "final_project" in dblist:
    # 	print("Database exists")

    # 3:Creat set
    set1=db.data
    return set1

def insertToMongoDB(set1):
	with open('population1.csv','r',encoding='utf-8')as csvfile:
		reader=csv.DictReader(csvfile)
		counts=0
		for each in reader:
			each['Year']=int(each['Year'])
			each['County Name']=str(each['County Name'])
			each['Population']=int(each['Population'])
			set1.insert_one(each)
			counts+=1
	print(counts)

set1 = connection()
insertToMongoDB(set1)