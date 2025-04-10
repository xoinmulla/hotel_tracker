from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('guest/<int:pk>/', views.guest_detail, name='guest_detail'),
    path('guests/', views.guest_list, name='guest_list'),  # Adjusted URL for guest list
]
