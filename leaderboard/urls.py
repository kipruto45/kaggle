from django.urls import path
from . import views

app_name = 'leaderboard'
urlpatterns = [
    path('competition/<int:competition_id>/', views.leaderboard_view, name='competition_leaderboard'),
]
