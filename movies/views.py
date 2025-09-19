from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm

def home(request):
    movies = Movie.objects.order_by('-created_at')
    return render(request, 'movies/home.html', {'movies': movies})

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

# --- new view for updating a movie ---
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form, 'movie': movie})

# --- new view for deleting a movie ---
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')
    return render(request, 'movies/delete_movie.html', {'movie': movie})

