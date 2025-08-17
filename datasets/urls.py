from django.urls import path
from . import views

app_name = 'datasets'
urlpatterns = [
    path('upload/', views.upload_dataset, name='upload'),
    path('list/', views.list_datasets, name='list'),
]
