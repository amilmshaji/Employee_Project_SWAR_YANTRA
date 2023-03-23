



from django.urls import path, include

from . import views

urlpatterns = [
    path('department',views.Department,name='department'),
    path('employee', views.Employee, name='employee'),

]