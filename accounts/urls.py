from django.urls import path
from .views import login_view, registration_view


urlpatterns = [
    path('login/', login_view, name='auth_login'),
    path('register/', registration_view, name='auth_register'),
]