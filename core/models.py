from django.db import models

# Create your models here.
class Article(models.Model):
    title =  models.CharField(max_length=250)
    body = models.TextField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title

