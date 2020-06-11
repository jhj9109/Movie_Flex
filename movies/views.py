from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Movie, Review, Comment
from .forms import ReviewForm, CommentForm

# Movie
@require_http_methods(['GET'])
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)

@require_http_methods(['GET'])
def detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        context = {
            'movie': movie
        }
        return render(request, 'movies/detail.html', context)

# Review
def review_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=movie_pk)
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.movie = movie
                review.save()
            return redirect('movies:detail', movie.pk)
        else:
            form = ReviewForm()
        context = {
            'form': form
        }
        return render(request, 'movies/review_form.html', context)
    else:
        messages.warning(request, '리뷰 작성을 위해서는 로그인이 필요합니다.')
        return redirect('accounts:login')


def review_detail(reqeust, movie_pk, reivew_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=reivew_pk)







