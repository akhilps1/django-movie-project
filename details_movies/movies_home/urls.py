
from django.urls import path
from . import views

app_name = 'movies_home'
urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:movie_id>/', views.update, name='update'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie')
]
