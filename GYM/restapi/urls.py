from django.urls import path
from restapi.views import *
urlpatterns=[
    path('apiGet',get_gymClassDetail),
    path('apiGet/<int:Id>',Up_Del_viw_by_ID) 
    # path('pag/<int:Id>',pag)  
]