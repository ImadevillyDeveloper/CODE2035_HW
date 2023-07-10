from django.urls import path
from .views import index, top_sellers,profile,login,register,advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('advertisement-post', advertisement_post, name='advertisement-post'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('profile', profile, name='profile'),
    path('top-sellers', top_sellers, name='top-sellers')
]