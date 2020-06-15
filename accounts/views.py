
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib import messages
# from rest_framework.decorators import api_view


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

# @login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('movies:index')
    form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# @login_required
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username) # user != person (프로필페이지 주인)
    like_movies = person.like_movies.all()

    followers = person.followers.all()
    followings = person.followings.all()
    context = {
        'person': person,
        'like_movies': like_movies,
        'followers': followers,
        'followings': followings,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username) # user != person(프로필페이지 주인)
    if person.followers.filter(username=request.user.username).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
