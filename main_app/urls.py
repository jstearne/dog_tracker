from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    # dogs/ --> READ (list)
    # dogs/<int:pk>/ --> Individual Dog Detail
    # dogs/new/ --> CREATE
    # dogs/<int:pk>/update --> EDIT
    # dogs/<int:pk>/delete --> DELETE
]
