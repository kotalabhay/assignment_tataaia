from django.apps import AppConfig
import os
import csv
from .models import Complaint_Data
import datetime

class ComplaintsConfig(AppConfig):
    name = 'complaints'

    def ready(self):
        format_str = '%d/%m/%Y'  # The format
        print(datetime_obj.date())
        workpath = os.path.dirname(os.path.abspath('views.py')) #Returns the Path your .py file is in
        c = open(os.path.join(workpath, '/csv/Consumer_Complaints_Data.csv'), 'rb')
        reader = csv.reader(c)

        for i,row in enumerate(reader):
            if i==0:
                pass
            else:
                row= "".join(row)
                row=row.replace(";"," ")
                row=row.split()
                ticket_id= row[0]
                date_of_issue= datetime.datetime.strptime(row[1], format_str)
                form_data= row[2]
                method= row[3]
                issue= row[4]
                caller_id_no= row[5]
                type_of_call_message= row[6]
                advertiser_business_np= row[7]
                city= row[8]
                Complaint_Data.objects.create(
                    ticket_id= int(ticket_id) ,
                    date_of_issue=  date_of_issue.date() ,
                    form_data= form_data ,
                    method=  method,
                    issue=  issue,
                    caller_id_no= caller_id_no,
                    type_of_call_message=  type_of_call_message,
                    advertiser_business_np=  advertiser_business_np,
                )
            c.close()