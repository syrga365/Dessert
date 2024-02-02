from django import forms

from post.models import Dessert, ReviewDessert, Category


class DessertCreateForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = ('title', 'photo', 'recipe', 'content', 'category')
        labels = {
            'title': "Название",
            "photo": "фото",
            "recipe": "рецепт",
            "content": "описание",
            "category": "категория"
        }


class ReviewDessertCreateForm(forms.ModelForm):
    class Meta:
        model = ReviewDessert
        fields = ('text',)
        labels = {
            'text': "Отзыв"
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        labels = {
            'title': "Категория"
        }
