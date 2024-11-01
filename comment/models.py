from django.db import models

# Create your models here.

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField()

    def __str__(self):
        return f'{self.user_name}: {self.content}'
