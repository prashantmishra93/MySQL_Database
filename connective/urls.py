from django.urls import path
from . import views

urlpatterns = [
    path('', views.success, name='home'),
    path('reg', views.Contactform, name='reg'),
    path('login', views.logindata, name='log'),
    path('logout', views.logout, name='logout'),
    path('show', views.show, name='show'),
]