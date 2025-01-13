from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('projects/', views.project, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('newsletter/', views.newsletter, name='newsletter')
]
