import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.


def home(request):
    movies = Movie.objects.all()
    context = {
        'movie_lists': movies,
    }
    return render(request, 'home.html', context)


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    obj = movie.movie_tag
    tags = re.sub('/', ',', obj)
    context = {
        'movie_detail': movie,
        'tags': tags
    }
    return render(request, 'detail.html', context)


# add movie function
def add_movie(request):
    # fetching data from input fields
    if request.method == 'POST':
        movie_title = request.POST.get('movie_title')
        movie_description = request.POST.get('movie_description')
        yearof_release = request.POST.get('yearof_release')
        movie_thumbnail = request.FILES['movie_thumbnail']
        movie_rating = request.POST.get('movie_rating')
        movie_tag = request.POST.get('movie_tag')
        # updating data to database
        movie = Movie(movie_title=movie_title,
                      movie_description=movie_description,
                      yearof_release=yearof_release,
                      movie_thumbnail=movie_thumbnail,
                      movie_rating=movie_rating, movie_tag=movie_tag)
        movie.save()
    return render(request, 'add.html')


# update movie function
def update(request, movie_id):
    # fetching movie id from database
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'movie': movie, 'form': form})


def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('/')


def rate_movie(request):
    return redirect('movie_detail')
