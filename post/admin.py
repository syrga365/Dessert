from django.contrib import admin
from post.models import Dessert
# Register your models here.


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']