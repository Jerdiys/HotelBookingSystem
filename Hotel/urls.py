from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('rooms/', views.Rooms, name='Rooms'),
    path('register/', views.Registration, name='Registration'),
    path('login/', views.Login, name='Login'),
    path('booking/', views.BookRoom, name='booking'),
    path('search/', views.search_booking, name='search_booking'),
    path('booking_success/<str:booking_code>/', views.booking_success, name='booking_success'),
    path('search_booking/<str:booking_code>/', views.search_booking, name='booking_detail')
]