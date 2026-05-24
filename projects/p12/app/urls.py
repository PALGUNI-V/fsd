from django.urls import path
from . import views

urlpatterns=[

path('',views.home),

path('save/',views.save),

path('update/',views.update),

path('displayall/',views.displayall)

]