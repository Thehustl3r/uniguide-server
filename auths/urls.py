from django.urls import path
from . import views

urlpatterns = [
    # re_path('', views.index),
    path('login', views.login),
    path('signup', views.signup),
    path('testtoken', views.test_token),

]