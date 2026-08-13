from django.shortcuts import render
from .forms import MovieForm

def add_movie(request):
    message = ''

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()

            message = f"Movie saved: {movie.name} ({movie.release_year})"
            form = MovieForm()
    else:
        form = MovieForm()

    return render(request, 'movie.html', {
        'form': form,
        'message': message
    })
