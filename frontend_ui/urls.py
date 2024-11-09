from django.urls import path
from . import views

app_name = 'frontend_ui'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_resource, name='add_resource'),
]
