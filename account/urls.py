from django.urls import path
from .import views

urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout, name="logout"),


]
