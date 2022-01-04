import datetime
import csv
import os






format_str = '%m/%d/%Y'  # The format
workpath = os.getcwd()
workpath = workpath + '/Consumer_Complaints_Data.csv'
c = open(workpath, 'r')
reader = csv.reader(c)

for i,row in enumerate(reader):
	if i==0:
            pass
	else:

  
            print(row[1])

            

c.close()


