from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    context = models.CharField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='Comment', blank=True, null=True)
    user_name = models.CharField(max_length=50)
    context = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name
