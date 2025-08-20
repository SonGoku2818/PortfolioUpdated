from django.urls import path
from .views import home,superuser

urlpatterns = [
    path('', home, name='home'),
    path('superuser/', superuser, name='superuser'),
]
