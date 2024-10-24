from django.urls import include, path

from service import views

app_name = 'service'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='calendar'),
    path('services/', views.services, name='services'),
    path('vision/', views.vision, name='vision'),
    path('service/<int:id>/details/', views.service_details, name='details'),
]
 