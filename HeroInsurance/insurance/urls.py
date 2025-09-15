from django.urls import path
from . import views

# Register your app urls
urlpatterns = [
    path('', views.index, name='index'),
    # if you use separate login page => path('login/', views.login_user, name='login'),
]