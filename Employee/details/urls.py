



from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Department,name='department'),
    path('employee', views.Employee, name='employee'),

]