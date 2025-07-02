from django.contrib import admin 

from django.urls import path 
from . import views

urlpatterns = [
     
    path('ML/', views.machine_learning),  
    path('rn/', views.random), 
    path('knn/', views.K_nearest), 
    path('dt/', views.decision_tree),
   # path('dl/', views.deep_learning),  
   # path('about/', views.about_us),
    
    
]
