from django.urls import path
from designmytee import views
from allauth.account.views import LoginView, SignupView, LogoutView,  PasswordResetView, EmailView

app_name = 'designmytee'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('results/', views.results, name='results'),
    path('competitions/', views.competitions, name='competitions'),
    path('myprofile/', views.myprofile, name = 'myprofile'),
    path('login/', LoginView.as_view(), name='account_login'),
    path('signup/', SignupView.as_view(), name='account_signup'),
    path('logout/', LogoutView.as_view(), name='account_logout'),
    path('password/reset/', PasswordResetView.as_view(), name='account_reset_password'),
    path('myprofile/email/', EmailView.as_view(), name='account_email'),
]
