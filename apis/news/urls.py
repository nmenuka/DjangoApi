from django.urls import path 
from apis.news import views

urlpatterns = [
    path('', views.NewsApiView.as_view())

]
