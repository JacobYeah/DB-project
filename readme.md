# Readme.md

## 1.Purpose

Through this project, we planned to find out the relations within some datasets of New York City,
which means all the datasets are based on the situation of New York City.
Following are the datasets:
18 and Older Adult Arrests;
Average Income and Tax Liability of Full Year Residents;
Index Crimes; 
Law Enforecement Personnel;
Population;
Recidivism.
Because we think some of the factors referred to above may have effects on the others. 
For instance, the number of law enforcement personnel and area economy may affect the number of arrests;
the first time arrest and recidivism may have a ratio in someplace.

## 2.Requirement

Python3
MongoDB
PostgreSQL
Pandas
pymongo

## 3.Usage

### Set-Up Database Preparation

Make sure the packages and software are installed in the test machine. 
Open up any terminal app(e.g. macOS - Teriminal.app, Windows - CMD and etc.).
Keep the PostgreSQL and MongoDB open. 

Note: Please keep the configuration of the folder when you download.

### Import Data

Change the current directory to this repo's root directory and
Create new Database: `psql -U postgres postgres < ./setup/setup.sql`
Create new Tables: `psql -U dbms_project_user dbms_final_project< ./setup/schema.sql`<br>Download dataset:` python retrieve_data.py`<br>Modify the dataset: `python modify_data.py`  <br>Import the csv file into PostgreSQL database, after enter the setup folder: `python load_data.py`
Import the csv file into MongoDB,after enter the setup folder:` python load_mongo.py`

### Start Up The Application

Run the application: `python application.py`
The terminal will show the options: Get use of different functions by typing in the corresponding number (Or q for quitting)

#### Cirme Information

It will provide NYC crime information by giving following choices.

##### When select Law Enforcement Table, it will three choices:

​		Select specific PD agency or Select specific county or Quit
​		Choose PD and input [PD] will get the result for law enforcement situation of specific PD
​		Choose county and input [county] will get the result for law enforcement situation of specific county
​		Choose q to quit

##### When select Recidivism Table, it will three choices:

​		Select specific year or Select specific age or Quit
​		Choose year and input [year] will get the result for recidivism situation of specific year
​		Choose age and input [age] will get the result for recidivism situation of specific age
​		Choose q to quit	

##### When select Index Crime Table, it will three choices:

​		Select specific year or Select specific county or Quit
​		Choose year and input [year] will get the result for index crime situation of specific year
​		Choose county and input [county] will get the result for index crime situation of specific county
​		Choose q to quit	

##### When select Adult Arrest Table, it will three choices:

​		Select specific year or Select specific county or Quit
​		Choose year and input [year] will get the result for adult arrest situation of specific year
​		Choose county and input [county] will get the result for adult arrest situation of specific county
​		Choose q to quit	

#### Income Information

It will provide NYC income information by giving following choices.
	There are three choices:
	Select specific year or Select specific county or Quit
	Choose year and input [year] will get the result for income situation of specific year
	Choose county and input [county] will get the result for income situation of specific county
	Choose q to quit

#### Population Information

It will provide NYC population information by giving following choices.
	There are two choices:
	Enter [year] and [county] will fetch the result of population in specific year and specific county
	Choose q to quit

#### Hybrid Information

It will provide the hybrid relation from multiple tables by giving following choices.

##### Number of arrested persons and police stations in specific areas in a specific year

​		Enter [year] and [county] to order specific year and county

##### Total population of a specific area and all cases in a specific year

​		Enter [year] and [county] to order specific year and county

##### Average income of all regions in a given year and data on all cases and light drug abuse cases

​		Enter [year] to order specific year

##### Number of full-time personnel and cases handled by each police station in a specific area in a specific year

​		Enter [year] and [county] to order specific year and county

##### Total number of crimes and the total number of recidivism in each region in a specific year, and the recidivism ratio

​		Enter [year] to order specific year

#### Quit

It will quit the whole application in the terminal by entering [q]

## 4. Reference Dataset

1. Adult Arrests 18 and Older by County
	Location of data: https://data.ny.gov/Public-Safety/Adult-Arrests-18-and-Older-by-County-Beginning-197/rikd-mt35
	License: Public
2. Average Income and Tax Liability of Full-Year Residents by County
	Location of data: https://data.ny.gov/Government-Finance/Average-Income-and-Tax-Liability-of-Full-Year-Resi/2w9v-ejxd
	License: Public
3. Index Crimes by County and Agency 
	Location of data: https://data.ny.gov/Public-Safety/Index-Crimes-by-County-and-Agency-Beginning-1990/ca8h-8gjq
	License: CC0: Public Domain (No copyright)
4. Law Enforcement Personnel by Agency 
	Location of data: https://data.ny.gov/Public-Safety/Law-Enforcement-Personnel-by-Agency-Beginning-2007/khn9-hhpq
	License: Public
5. New York State Population Data
	Location of data: https://health.data.ny.gov/Health/New-York-State-Population-Data-Beginning-2003/e9uj-s3sf
	License: CC0: Public Domain (No copyright)
6. Recidivism
	Location of data: https://data.ny.gov/Public-Safety/Recidivism-Beginning-2008/y7pw-wrny
	License: Public



