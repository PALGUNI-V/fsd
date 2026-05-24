from django.urls import path
from . import views

urlpatterns=[

path('',views.home),

path('display/',views.display),

path('displayall/',views.displayall)

]