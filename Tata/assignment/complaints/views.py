from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.filters import SearchFilter , OrderingFilter
from rest_framework.parsers import JSONParser
from .serializers import  ComplaintSerializer , BulkComplaintSerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.db.models import Q
import os
import csv

from time import time
from .models import Complaint_Data
import datetime
from pytz import utc



        # put your startup code here
# Create your views here.



class ComplaintView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.DestroyModelMixin):

    queryset =Complaint_Data.objects.all()
    serializer_class = ComplaintSerializer
    filter_backends = [SearchFilter]
    search_fields= ['state','city','issue']

    def get_queryset(self, *args, **kwargs):
        queryset = Complaint_Data.objects.all()
        query= self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                    Q(state__icontains= query) |
                    Q(issue__icontains= query)
            )
        return queryset.order_by('date_of_issue')

    def create(self, request, *args, **kwargs):
        # if the data is a dictionary, use parent create that relies on serializer_class
        if isinstance(request.data, dict):
            return super(ComplaintView, self).create(request, *args, **kwargs)
        # if the data is a list, send to the bulk serializer to handle creation
        elif isinstance(request.data, list):
            serializer = BulkComplaintSerializer(data= {'complaint': request.data})
            if serializer.is_valid():
                serializer.create(request.data)
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response('Invalid data received', status=400)




@csrf_exempt
def insert_csv_data(request):
    try:
        start = time()
        list_data=[]
        format_str = '%m/%d/%Y'  # The format
        workpath = os.path.dirname(os.path.abspath('views.py'))
        workpath = workpath + '/complaints/csv/Consumer_Complaints_Data.csv'
        c = open(workpath, 'r')
        reader = csv.reader(c)

        for i,row in enumerate(reader):
            if i==0:
                pass
            else:

                ticket_id = int(row[0])
                date_of_issue = str(row[1]).strip(' ')
                time_of_issue = row[2]
                form_data= row[3]
                method= row[4]
                issue= row[5]
                caller_id_no= row[6]
                type_of_call_message= row[7]
                advertiser_business_np= row[8]
                city= row[9]
                state = row[10]
                zip = row[11]
                location = row[12]
                # ticket_id = data.pop('ticket_id', None)
                # date_of_issue = data.pop('date_of_issue', None)
                # time_of_issue = data.pop('time_of_issue', None)
                # form_data = data.pop('form_data', None)
                # method = data.pop('method', None)
                # issue = data.pop('issue', None)
                # caller_id_no = data.pop('caller_id_no', None)
                # type_of_call_message = data.pop('type_of_call_message', None)
                # advertiser_business_np = data.pop('advertiser_business_np', None)
                # city = data.pop('city', None)
                # state = data.pop('state', None)
                # zip = data.get('zip', None)
                # location = data.pop('location', None)
                if (date_of_issue == None or  date_of_issue =="" or  date_of_issue ==" ") :
                    date_of_issue = None
                else:
                    for fmt in ('%m/%d/%Y','%Y/%m/%d', '%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d',  '%m-%d-%Y'):
                        try:
                            date_of_issue = datetime.datetime.strptime(date_of_issue, fmt).date()
                            break
                        except ValueError:
                            pass
                        #raise ValueError('no valid date format found')
                data = {
                'ticket_id': ticket_id ,
                'date_of_issue' : date_of_issue ,
                'time_of_issue' : time_of_issue ,
                'form_data' : form_data ,
                'method' :  method,
                'issue' :  issue,
                'caller_id_no' : caller_id_no,
                'type_of_call_message' :  type_of_call_message,
                'advertiser_business_np' : advertiser_business_np,
                'city' : city ,
                'state' : state ,
                'zip' : zip,
                'location' : location ,
                }
                list_data.append(data)
        c.close()
        create_objects_list = [Complaint_Data(**vals) for vals in list_data]
        Complaint_Data.objects.bulk_create(create_objects_list)
        stop = time()
        message ='{0} items added in {1} seconds'.format(i,stop-start)
        return JsonResponse(message, status=201 ,safe=False)
    except Exception as e:
        message = 'failed to save' + str(e)
        return JsonResponse(message, status=400 ,safe=False)

# @csrf_exempt
# def save_view_data(request):
#
#
#     if request.method== 'GET' :
#
#         data = get_csv_data()
#         data= data[:18]
#         print('GET got executed')
#         serializer = ComplaintSerializer(data, many=True)
#         return  JsonResponse(serializer.data , status=201, safe=False)
#
#     elif request.method=='POST':
#         data= JSONParser().parse(request)
#         print('POST got executed')
#         #print(data)
#         bulk_serializer = BulkComplaintSerializer(data=data , many=True)
#         if bulk_serializer.is_valid():
#             bulk_serializer.create(data)
#             return  JsonResponse(bulk_serializer.data , status=201 , safe=False)
#         return  JsonResponse(bulk_serializer.errors , status=400 , safe=False)



