from django.urls import path
from .views import dataload, dataretrieve

app_name = 'backup'

urlpatterns = [
    path('', dataload, name='dataload'),
    path('retrieve/', dataretrieve, name='retrieve')
]
