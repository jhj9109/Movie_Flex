from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # Movie
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),

    # Review
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/review_detail/<review_pk>/', views.review_detail, name='review_detail'),

]
