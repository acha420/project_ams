from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('update/<int:id>/', views.update_show, name='update_show'),
path('delete/<int:id>/', views.delete_show, name='delete_show'),
path('my-shows/', views.my_shows, name='my_shows'),
path('profile/', views.profile_update, name='profile_update'),
]