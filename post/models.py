from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.title}'


class Dessert(models.Model):
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts',
        null=True
    )
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/%Y/%m/%d", null=True)
    content = models.TextField()
    recipe = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name="category")


class ReviewDessert(models.Model):
    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        null=True
    )
    posts = models.ForeignKey(
        'post.Dessert',
        on_delete=models.CASCADE,
        related_name="review"
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
