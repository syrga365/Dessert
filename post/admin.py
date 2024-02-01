from django.contrib import admin
from post.models import Dessert, Category, ReviewDessert
# Register your models here.


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ReviewDessert)
