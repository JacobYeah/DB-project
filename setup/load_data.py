import os
import pandas as pd
import psycopg2

try:
	os.chdir(os.getcwd())
	print(os.getcwd())
except:
	pass

csv_dirname = '../CSV'  

def find_csv_filenames(path_to_dir, suffix=".csv"):
    filenames = os.listdir("%s" % path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]

csv_name_list = find_csv_filenames(csv_dirname)
print(csv_name_list)

def import_csv():

	for csv_name in csv_name_list:
		csv_path = os.path.join(os.getcwd(), os.path.expanduser(csv_dirname), csv_name)
		print(csv_name.replace('.csv',''))

		databasename = csv_name.replace('.csv','')

		try:
			os.system("psql -d dbms_final_project -c \"COPY %s FROM \'%s\' WITH(FORMAT csv);\"" % (databasename, csv_path) )
		except:
			print("Cannot COPY csv: %s" % csv_name)

import_csv()