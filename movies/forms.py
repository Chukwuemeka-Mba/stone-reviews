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

class ReviewForm(forms.Form):
    title = forms.ChoiceField()
    author = forms.ChoiceField()
    details = forms.CharField(label='Review', max_length=3000, widget=forms.Textarea)