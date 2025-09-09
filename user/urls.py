from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login_page'),
    path('register/', register_view, name='register_page'),
    path('logout/', logout_view, name='logout_page'),
    path('change-password/', change_password_view, name='change_password_page'),
]
