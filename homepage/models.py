from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField()
    candle_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.title:
            return f"{self.title} ({self.user.username})"
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

