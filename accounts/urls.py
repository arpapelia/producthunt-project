

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_auth, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
