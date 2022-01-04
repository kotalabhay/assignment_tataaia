from rest_framework import serializers
from .models import Complaint_Data
import os
import csv
import datetime

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model= Complaint_Data
        fields=['ticket_id','date_of_issue','form_data','method','issue','caller_id_no','type_of_call_message','advertiser_business_np','city','state','zip','location']
        read_only_fields = ['id']

class BulkComplaintSerializer(serializers.Serializer):
    complaint = ComplaintSerializer(many=True)

    class Meta:
        fields=['ticket_id','date_of_issue','time_of_issue','form_data','method','issue','caller_id_no','type_of_call_message','advertiser_business_np','city','state','zip','location']
        read_only_fields = ['id']

    def create(self, validated_data):
            # store the  objects  in bulk
        format_str = '%m/%d/%Y'  # The format
        dict_list=[]
            # iterate over the validated_data and add Complaint objects to a list to be created
        for data in validated_data:
                # notice the same functionality from the regular serializer
            print(data)
            ticket_id = data.get('ticket_id', None)
            date_of_issue = data.get('date_of_issue', None)
            time_of_issue = data.get('time_of_issue', None)
            form_data = data.get('form_data', None)
            method = data.get('method', None)
            issue = data.get('issue', None)
            caller_id_no= data.get('caller_id_no', None)
            type_of_call_message = data.get('type_of_call_message', None)
            advertiser_business_np = data.get('advertiser_business_np', None)
            city = data.get('city', None)
            state = data.get('state', None)
            zip= data.get('zip', None)
            location = data.get('location', None)
            if (date_of_issue == None or  date_of_issue =="" or  date_of_issue ==" "):
                date_of_issue = None
            else:
                for fmt in ('%Y/%m/%d', '%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d' ,'%m/%d/%Y', '%m-%d-%Y'):
                    try:
                        date_of_issue = datetime.datetime.strptime(date_of_issue, fmt).date()
                        break
                    except ValueError:
                        pass
            # complaint_obj = Complaint_Data.objects.get_or_create (
            #         ticket_id=ticket_id,
            #         date_of_issue= date_of_issue if date_of_issue == None else date_of_issue.date(),
            #         form_data= form_data,
            #         method=method,
            #         issue=issue,
            #         caller_id_no=caller_id_no,
            #         type_of_call_message=type_of_call_message,
            #         advertiser_business_np=advertiser_business_np,
            #         city=city,
            #         state= state,
            #         zip=zip,
            #         location=location,
            # )[0]

            data = {
                    'ticket_id': ticket_id,
                    'date_of_issue': date_of_issue,
                    'time_of_issue': time_of_issue,
                    'form_data': form_data,
                    'method': method,
                    'issue': issue,
                    'caller_id_no': caller_id_no,
                    'type_of_call_message': type_of_call_message,
                    'advertiser_business_np': advertiser_business_np,
                    'city': city,
                    'state': state,
                    'zip': zip ,
                    'location': location,
                }

            dict_list.append(data)
                # make it as Django objects list
        create_objects_list= [Complaint_Data(**vals) for vals in dict_list] # converted to objects
        return Complaint_Data.objects.bulk_create(create_objects_list)

    # ticket_id= serializers.AutoField(primary_key=True)
    # date_of_issue= serializers.DateField()
    # form_data= serializers.CharField(max_length=100)
    # method= serializers.CharField(max_length=100)
    # issue= serializers.CharField(max_length=100)
    # caller_id_no= serializers.CharField(max_length=100)
    # type_of_call_message= serializers.CharField(max_length=100)
    # advertiser_business_np= serializers.CharField(max_length=100)
    # city= serializers.CharField(max_length=100)
    #
    #
    #
    # def create(self, validated_date):
    #     return Complaint_Data.objects.create(validated_data)
    #
    # def update(selfself,instance,validated_data):
    #     instance.ticket_id= validated_data.get('ticket_id',instance.ticket_id)
    #     instance.date_of_issue = validated_data.get('date_of_issue', instance.date_of_issue)
    #     instance.form_data = validated_data.get('form_data', instance.form_data)
    #     instance.method = validated_data.get('method', instance.method)
    #     instance.issue = validated_data.get('issue', instance.issue)
    #     instance.caller_id_no = validated_data.get('caller_id_no', instance.caller_id_no)
    #     instance.type_of_call_message= validated_data.get('type_of_call_message', instance.type_of_call_message)
    #     instance.advertiser_business_np = validated_data.get('advertiser_business_np', instance.advertiser_business_np)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance