from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('projects/', views.projects_view, name='projects'),
    path('resume/', views.resume_view, name='resume'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
]
