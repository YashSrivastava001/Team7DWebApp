from django.urls import path
from designmytee import views

app_name = 'designmytee'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('results/', views.results, name='results'),
    path('competitions/', views.competitions, name='competitions'),
    path('signin/', views.signin, name='signin'),
]
