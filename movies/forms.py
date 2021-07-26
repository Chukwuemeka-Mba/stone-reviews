from django import forms
from .models import Movie, Review

class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'date_released',
            'rating',
        )

class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'author',
            'details',
        )
