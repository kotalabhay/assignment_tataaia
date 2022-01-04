
# Create your models here.
from django.db import models

class Complaint_Data(models.Model):
    id= models.AutoField(primary_key=True)
    ticket_id= models.IntegerField(null=True,blank=True)
    date_of_issue= models.DateField(null=True,blank=True)
    time_of_issue = models.CharField(max_length=100, null=True,blank=True)
    form_data=  models.CharField(max_length=100, null=True,blank=True)
    method= models.CharField(max_length=100 ,null=True,blank=True)
    issue= models.CharField(max_length=100, null=True,blank=True)
    caller_id_no=models.CharField(max_length=100 , null=True,blank=True)
    type_of_call_message= models.CharField(max_length=100 ,null=True,blank=True)
    advertiser_business_np=models.CharField(max_length=100 , null=True,blank=True)
    city=models.CharField(max_length=100 , null=True,blank=True)
    state= models.CharField(max_length=100 , null=True,blank=True)
    zip= models.CharField(max_length=100 , null=True,blank=True)
    location=models.CharField(max_length=100, null=True,blank=True)
