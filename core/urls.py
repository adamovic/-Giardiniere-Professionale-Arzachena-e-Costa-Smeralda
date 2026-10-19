from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('galleria/', views.gallery, name='gallery'),
    path('contatti/', views.contact, name='contact'),
]
