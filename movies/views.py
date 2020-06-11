from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
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
        reviews = movie.reviews.all()
        context = {
            'movie': movie,
            'reviews': reviews,
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


def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comments = Comment.objects.filter(review=review)
    form = CommentForm()

    context = {
        'movie': movie,
        'review': review,
        'comments': comments,
        'form': form,
    }
    return render(request, 'movies/review_detail.html', context)

@login_required
def review_update(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    review = get_object_or_404(Review, id=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.movie = movie
                review.save()
                return redirect('movies:review_detail', movie.pk, review.pk)
        else:
            form = ReviewForm(instance=review)
        context = {
            'form': form
        }
        return render(request, 'movies/review_form.html', context)
    else:
        messages.warning(request, '리뷰작성자만 수정/삭제 가능합니다.')
        return redirect('movies:index')

@require_POST
@login_required
def review_delete(request, movie_id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user:
        review.delete()
        messages.warning(request, '리뷰가 삭제 되었습니다.')
    return redirect('movies:detail', movie_id)




