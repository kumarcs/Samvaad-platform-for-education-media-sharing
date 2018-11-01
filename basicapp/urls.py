from django.urls import path
from basicapp import views

app_name = 'basicapp'
urlpatterns = [
    path('', views.user_login, name='login'),
]
