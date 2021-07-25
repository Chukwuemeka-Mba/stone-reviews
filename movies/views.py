from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from django.views.generic import TemplateView, DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Movie, Review
from .forms import MovieModelForm, ReviewForm


class LandingPageView(TemplateView):
	template_name = "landing.html"

class MovieListView(ListView):
	template_name = "leads/lead_list.html"
	queryset = Movie.objects.all()
	context_object_name = "movies"

class MovieDetailView(DetailView):
	template_name = "movie_detail.html"
	queryset = Movie.objects.all()
	context_object_name = "movie"

class MovieUpdateView(UpdateView):
	template_name = "movie_update.html"

class MovieDeleteView(DeleteView):
	template_name = "movie_delete.html"

def landing_page(request):
	return render(request, "landing.html")


# def movie_list(request):
# 	movies = Movie.objects.all()
# 	context = {
#         "movies": movies
#     }
# 	return render(request, "movies/movie_list.html", context)

def movie_detail(request, pk):
	movies = Movie.objects.get(id=pk)
	reviews = Review.objects.filter(title=movies)
	context = {
        "movies": movies,
		"reviews": reviews
    }
	return render(request, "movies/movie_detail.html", context)

def movie_create(request):
	if request.method == 'POST':
		print('Recieving a post request')
		form = MovieModelForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/movies")	
	context = {
		"form": MovieModelForm()
	}
	return render(request, "movies/movie_create.html", context)

def movie_update(request, pk):
	movie = Movie.objects.get(id=pk)
	form = MovieModelForm(instance=movie)
	if request.method == "POST":
		form = MovieModelForm(request.POST, instance=movie)
		if form.is_valid():
			form.save()
		return redirect("/movies")
	context = {
		"form": form,
		"movie": movie
	}
	return render(request, "movies/movie_update.html", context)

def movie_delete(request, pk):
	movie = Movie.objects.get(id=pk)
	movie.delete()
	context = {
		"movie" : movie
	}
	return render(request, "movies/movie_delete.html", context)

def review_create(request, pk):
	movie = Movie.objects.get(id=pk)
	if request.method == 'POST':
		print('Recieving a post request')
		form = ReviewForm(request.POST)
		if form.is_valid():
			print("The form is valid")
			print(form.cleaned_data)
			movie.title = form.cleaned_data['title']
			author = form.cleaned_data['author']
			details = form.cleaned_data['details']
			Review.objects.create(
				title=movie.title,
				author=author,
				details=details
			)
		return redirect("/movies")	
	context = {
		"movie": movie,
		"form": ReviewForm()
	}
	return render(request, "movies/review_create.html", context)





#--------------------------------------------------

# #def movie_create(request):
# 	if request.method == 'POST':
# 		print('Recieving a post request')
# 		form = MovieForm(request.POST)
# 		if form.is_valid():
# 			print("The form is valid")
# 			print(form.cleaned_data)
# 			title = form.cleaned_data['title']
# 			date_released = form.cleaned_data['date_released']
# 			rating = form.cleaned_data['rating']
			
# 			Movie.objects.create(
# 				title=title,
# 				date_released=date_released,
# 				rating=rating
# 			)
# 		return redirect("/movies")	
# 	context = {
# 		"form": MovieForm()
# 	}
# 	return render(request, "movies/movie_create.html", context)
