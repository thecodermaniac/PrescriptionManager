from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('signup',views.signup),
    path('logintemp',views.signin),
    path('login',views.login),
    path('dashbrd',views.dashboard),
    path('addPrescription',views.AddPrescrib)
]