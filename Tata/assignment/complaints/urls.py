from django.urls import path , include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'complaints/', ComplaintView, basename='complaints')
#router.register(r'insert_csv_data/', insert_csv_data, basename='insert_csv_data')
urlpatterns = router.urls
# urlpatterns = [
#     path('complaints/', save_view_data),
# ]

urlpatterns = [
    path('insert_csv_data/',insert_csv_data),
]

urlpatterns += router.urls
