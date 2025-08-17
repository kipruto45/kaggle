from django.urls import path
from . import views

app_name = 'discussion'
urlpatterns = [
    path('competition/<int:competition_id>/', views.thread_list, name='thread_list'),
    path('competition/<int:competition_id>/create/', views.create_thread, name='create_thread'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
]
