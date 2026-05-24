from django.urls import path
from . import views

urlpatterns=[

path('',views.home),

path('save/',views.save),

path('delete/',views.delete),

path('displayall/',views.displayall)

]