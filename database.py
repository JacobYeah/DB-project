import pandas as pd
import psycopg2
import psycopg2.extras

def crime_query(conn):

    while True:
        print("1. Law Enforcement Table.\n"
              "2. Recidivism Table.\n"
              "3. Index Crime Table.\n"
              "4. Adult Arrest Table\n"
              "q. Quit")
        choice = input("Input choice Here:")
        if choice == '1':
              print("Select Law Enforcement Table Successfully.\n")
              print("1. Select specific PD agency, enter\n"
                    "2. Select specific county, enter\n"
                    "To quit, enter q.\n")
              mode = input("Input mode here: ")
              if mode == '1':
                  print("Chose PD agency successfully!\n")
                  pd = input("Input PD agency here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM swornoffice WHERE pd=(%s)",(pd,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong pd, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=[ 'county','pd','year','fulltimetotal','partimetotal']
                      print(show)
              elif mode == '2':
                  print("Chose county successfully!\n")
                  county = input("Input full name of county here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM swornoffice WHERE county=(%s)",(county,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong county, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=[ 'county','pd','year','fulltimetotal','partimetotal']
                      print(show)   
              elif mode == 'q':
                  break
              else:
                  print("Invalid input! Please input again.\n")
        elif choice == '2':
              print("Select Recidivism Table Successfully.\n")
              print("1. Select specific year, enter\n"
                    "2. Select specific age, enter\n"
                    "To quit, enter q.\n")
              mode = input("Input mode here: ")
              if mode == '1':
                  print("Chose year successfully!\n")
                  year = input("Input year here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM recidivism WHERE year=(%s)",(year,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong year, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=[ 'year', 'county', 'gender', 'age']
                      print(show) 
              elif mode == '2':
                  print("Chose age successfully!\n")
                  age = input("Input age here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM recidivism WHERE age=(%s)",(age,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong age, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=[ 'year', 'county', 'gender', 'age']
                      print(show)
              elif mode == 'q':
                  break
              else:
                  print("Invalid input! Please input again.\n")
        elif choice == '3':
              print("Select Index Crime Table Successfully.\n")
              print("1. Select specific year, enter\n"
                    "2. Select specific county, enter\n"
                    "3. Select cases, enter\n"
                    "To quit, enter q.\n")
              mode = input("Input mode here: ")
              if mode == '1':
                  print("Chose year successfully!\n")
                  year = input("Input year here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM indexcrime WHERE year=(%s)",(year,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong year, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=['county','agency', 'year', 'indextotal']
                      print(show)
              elif mode == '2':
                  print("Chose county successfully!\n")
                  county = input("Input county here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM indexcrime WHERE county=(%s)",(county,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong county, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=['county','agency', 'year', 'indextotal']
                      print(show)
              elif mode == '3':
                  print("Chose year successfully!\n")
                  case = int(input("We'll provide the case number more than specific number, input case number here: "))
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM indexcrime WHERE indextotal>=%s",(case,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong number, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=['county','agency', 'year', 'indextotal']
                      print(show)
              elif mode == 'q':
                  break
              else:
                  print("Invalid input! Please input again.\n")      
        elif choice == '4':
              print("Select Adult Arrest Table Successfully.\n")
              print("1. Select specific year, enter\n"
                    "2. Select specific county, enter\n"
                    "To quit, enter q.\n")
              mode = input("Input mode here: ")
              if mode == '1':
                  print("Chose year successfully!\n")
                  year = input("Input year here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM adultarresta WHERE year=(%s)",(year,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong year, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=['county', 'year', 'totalcase', 'felonytotal', 'misdemeanortotal']
                      print(show)
              elif mode == '2':
                  print("Chose county successfully!\n")
                  county = input("Input county here: ")
                  cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
                  cursor.execute("SELECT * FROM adultarresta WHERE county=(%s)",(county,))
                  record=cursor.fetchall()
                  if(len(record)==0):
                      print("Wrong county, no record!\n")
                  else:
                      show = showRecord(record)
                      show.columns=['county', 'year', 'totalcase', 'felonytotal', 'misdemeanortotal']
                      print(show)
              elif mode == 'q':
                  break
              else:
                  print("Invalid input! Please input again.\n") 
        elif choice == 'q':
          break
        else:
          print("Invalid input! Please input again.\n")

              

def income_query(conn):
    while True:
        print("1. Select specific year, enter\n"
              "2. Select specific county, enter\n"
              "To quit, enter q.\n")
        choice = input("Input choice here: ")
        if choice == '1':
            print("Chose year successfully!\n")
            year = input("Input year here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("SELECT * FROM income WHERE year=(%s)",(year,))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong year, no record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'county', 'avgagi', 'avgtax']
                print(show)
        elif choice == '2':
            print("Chose county successfully!\n")
            county = input("Input full name of county here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("SELECT * FROM income WHERE county=(%s)",(county,))
            record=cursor.fetchall()
            if(len(record)==0):  ##here we need to check if record is none, which means no such county in the record, if it works, then add mode 3, select year and county at same time.
                print("Wrong county, no record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'county', 'avgagi', 'avgtax']
                print(show)
        elif choice == 'q':
            break
        else:
            print("Invalid input! Please input again.\n")
            
                
def hybrid_query(conn):
    while True:
        print("1. Select number of arrested persons and police stations in specific areas in a specific year\n"
              "2. Select total population of a specific area and all cases in a specific year\n"
              "3. Select average income of all regions in a given year and data on all cases and light drug abuse cases\n"
              "4. Select number of full-time personnel and cases handled by each police station in a specific area in a specific year\n"
              "5. Select total number of crimes and the total number of recidivism in each region in a specific year, and the recidivism ratio\n"
              "To quit, enter q.\n"
             )
        choice = input("Input choice here: ")
        if choice == '1':
            print("Chose number of arrested persons and police stations in specific areas in a specific year successfully!\n")
            year = input("Input year here: ")
            print("\n")
            county = input("Input county here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("select swornoffice.year as Year,swornoffice.county \
                            as county, sum(fulltimetotal),adultarresta.totalcase \
                            from \
                            swornoffice inner join adultarresta \
                            on swornoffice.year = adultarresta.year and swornoffice.county = adultarresta.county \
                            where swornoffice.year = (%s) and swornoffice.county = (%s) \
                            group by (swornoffice.year ,swornoffice.county, adultarresta.totalcase)",(year, county))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong , no such year or county in record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'county', 'totalCriminal', 'totalcase']
                print(show,'\n')
        elif choice == '2':
            print("Chose total population of a specific area and all cases in a specific year successfully!\n")
            year = input("Input year here: ")
            print("\n")
            county = input("Input county here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("select population.year,population.county, sum(popul) Popul,adultarresta.totalcase \
                            from \
                            population \
                            left join adultarresta \
                            on population.year = adultarresta.year and population.county = adultarresta.county \
                            where population.year = (%s) and population.county = (%s) \
                            group by (population.year,population.county,adultarresta.totalcase)",(year, county))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong , no such year or county in record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'county', 'Popul', 'totalcase']
                print(show, '\n')
        elif choice == '3':
            print("Chose average income of all regions in a given year and data on all cases and light drug abuse cases successfully!\n")
            year = input("Input year here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("select income.year, income.county, income.avgagi,foo.totalcase,foo.drugf \
                            from \
                            income \
                            left join \
                            (select adultarresta.year,adultarresta.county, adultarresta.totalcase,adultarrestb.drugf \
                            from \
                            adultarresta \
                            inner join adultarrestb \
                            on adultarresta.county = adultarrestb.county and adultarresta.year = adultarrestb.year) \
                            as foo \
                            on income.county =foo.county and income.year = foo.year \
                            where income.year = (%s) order by(income.avgagi)" ,(year,))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong , no such year in record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'county', 'avgagi', 'totalcase', 'drugf']
                print(show, '\n')  
        elif choice == '4':
            print("Chose number of full-time personnel and cases handled by each police station in a specific area in a specific year successfully!\n")
            year = input("Input year here: ")
            print("\n")
            county = input("Input county here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("select indexcrime.year,indexcrime.agency, indexcrime.county,indexcrime.indextotal,swornoffice.fulltimetotal \
                            from \
                            indexcrime \
                            inner join swornoffice \
                            on indexcrime.agency=swornoffice.pd and indexcrime.year =  swornoffice.year \
                            where indexcrime.year = (%s) and indexcrime.county = (%s) \
                            order by swornoffice.fulltimetotal",(year, county))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong , no such year or county in record!\n")
            else:
                show = showRecord(record)
                show.columns=['year', 'agency', 'county', 'Totalalert', 'Fulltimetotal']
                print(show, '\n') 
        elif choice == '5':
            print("Chose total number of crimes and the total number of recidivism in each region in a specific year, and the recidivism ratio successfully!\n")
            year = input("Input year here: ")
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            sql = "select adultarresta.county, adultarresta.year, adultarresta.totalcase,foo.count As recidivism, (round((cast(foo.count as numeric)/cast(adultarresta.totalcase as numeric))*100,2))||(%s) as Rate \
                            from \
                            adultarresta \
                            left join \
                            (select year, lower(county) as c, count(*) from recidivism group by (year, county)) as foo \
                            on adultarresta.year = foo.year and lower(adultarresta.county) = foo.c \
                            where adultarresta.year = (%s)"
            cursor.execute(sql,('%',year))
            record=cursor.fetchall()
            if(len(record)==0):
                print("Wrong , no such year in record!\n")
            else:
                show = showRecord(record)
                show.columns=['county', 'year', 'Totalcase', 'Recidivism','Rate']
                print(show, '\n')
        elif choice == 'q':
            break
        else:
            print("Invalid input! Please input again.\n")

        
        
def showRecord(record):
  # pd.set_option('display.max_columns', None)
  # pd.set_option('display.max_rows', None)
  result = pd.DataFrame(record)
  return result



def population_query(set1):
  while True:
    print("1. Query population\n"
          "q. Quit")

    choice = input("Input choice Here:")
    if choice == '1':
      print("Chose successfully!\n")
      print("Please wait for loading!\n")
      area = set()
      County1 = set1.find({},{'County Name':1})
      for con1 in County1:
        if(con1['County Name'] in area):
          continue
        else:
          area.add(con1['County Name'])
      year = int(input("Input year here: "))
      county = input("Input county here: ")
      if((year > 2017 or year < 2003) or (county not in area)):
        print('Wrong, no such record')
      else:
        amount = 0
        result = set1.find({'Year':year, 'County Name': county},{'Population':1})
        for pop in result:
          amount +=pop['Population']
        print('The population in '+ county + ' , ' + str(year) + ' is ' + str(amount)+'.\n')
    elif choice == 'q':
      break
    else:
      print("Invalid input! Please input again.\n")




  



        
        
        
        
        
        
        
     