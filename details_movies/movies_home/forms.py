
from .models import Movie
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'movie_title', 'movie_description', 'yearof_release', 'movie_thumbnail', 'movie_rating', 'movie_tag'
            ]

        widgets = {
            "movie_title": forms.TextInput(attrs={'class': 'form-control border-light border-opacity-50 bg-dborder-light border-opacity-50 bg-dark text-light'}),
            "movie_description": forms.Textarea(attrs={'class': 'form-control border-light border-opacity-50 bg-dark text-light'}),
            "yearof_release": forms.NumberInput(attrs={'class': 'form-control border-light border-opacity-50 bg-dark text-light'}),
            "movie_thumbnail": forms.FileInput(attrs={'class': 'form-control border-light bg-dark text-light opacity-50'}),
            "movie_rating": forms.NumberInput(attrs={'class': 'form-control border-light border-opacity-50 bg-dark text-light'}),
            "movie_tag": forms.TextInput(attrs={'class': 'form-control border-light border-opacity-50 bg-dark text-light'})

        }    