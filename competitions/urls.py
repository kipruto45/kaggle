from django.urls import path
from . import views

app_name = 'competitions'
urlpatterns = [
    path('list/', views.list_competitions, name='list'),
    path('create/', views.create_competition, name='create'),
    path('<int:pk>/', views.competition_detail, name='detail'),
    path('<int:pk>/submit/', views.submit_solution, name='submit'),
]
