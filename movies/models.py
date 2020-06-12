from django.db import models
from django.conf import settings


# 여기는 추후 영화진흥원API 통해서 DB 받아와야함.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.URLField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies') # related : 유저가 좋아요한 영화들


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews') # 유저가 삭제되면 리뷰도 삭제됨.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews') # related : 유저가 좋아요한 리뷰들


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

