from django.urls import path 
from apis.accounts import views

urlpatterns = [
    path('', views.CreateUserApiView.as_view())

]
