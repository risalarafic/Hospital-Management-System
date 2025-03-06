from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index), #mapping the url from the projects url to the corresponding views 
    path('about/', views.about),
    path('booking/', views.booking),
    path('doctors/', views.doctors),
    path('contact/', views.contact), 
    path('department/', views.department),
]