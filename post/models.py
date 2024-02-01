from django.db import models

# Create your models here.


class Dessert(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", null=True)
    content = models.TextField()
    recipe = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)