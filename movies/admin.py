from django.contrib import admin

from .models import Movie, Review

# admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Review)