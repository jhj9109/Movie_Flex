from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    # Movie
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),

    # Review
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/review_detail/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/review_update/<int:review_pk>/', views.review_update, name='review_update'),
    path('<int:movie_pk>/review_delete/<int:review_pk>/', views.review_delete, name='review_delete'),

]
