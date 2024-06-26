from django.contrib import admin
from post.models import Dessert, Category, ReviewDessert


# Register your models here.


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ["user", 'title', 'created_at']
    fields = ["id", "title", "user", "content", 'recipe', "photo", "category", "rate", "created_at", "updated_at"]
    readonly_fields = ["id", "created_at", "updated_at"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']


admin.site.register(ReviewDessert)
