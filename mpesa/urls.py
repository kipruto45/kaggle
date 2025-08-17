from django.urls import path
from . import views

app_name = 'mpesa'
urlpatterns = [
    path('payout/', views.payout, name='payout'),
]
