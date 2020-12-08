import psycopg2
import os
from pymongo import MongoClient
import database

if __name__ == '__main__':
    HOST = 'localhost'
    DBNAME = 'dbms_final_project'
    USER = 'dbms_project_user'
    PASSWORD = 'dbms_password'

    conn_string = "host=%s dbname=%s user=%s password=%s" % (HOST, DBNAME, USER, PASSWORD)
    conn = psycopg2.connect(conn_string)

    mongoconn = MongoClient('mongodb://localhost:27017/')
    db=mongoconn.final_project
    set1 = db.data



    
    while True:

        mode = input("Welcome to NYC Information Database\n--- Mode Select ---\n 1. Crime Information\n 2. Income Information \n 3. Population Information\n 4. Hybrid Information\n q. Quit\n\nEnter here: ")
        if mode == '1':
            database.crime_query(conn)
        elif mode == '2':
            database.income_query(conn)
        elif mode == '3':
            database.population_query(set1)
        elif mode == '4':
            database.hybrid_query(conn)
        elif mode == 'q':
            break
        else: 
            print("Invalid input! Please input again.\n")



   