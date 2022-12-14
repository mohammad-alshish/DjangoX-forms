from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Game(models.Model):
    title = models.CharField(max_length=64)
    developer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", args=[str(self.id)])
