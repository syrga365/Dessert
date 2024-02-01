from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from post.models import Dessert, Category


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello, It's my project")


def current_date_view(request):
    if request.method == 'GET':
        current_datetime = datetime.now()
        return HttpResponse(current_datetime)


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Good bye, user!!!")


def dessert_posts_view(request):
    if request.method == "GET":
        dessert_posts = Dessert.objects.all()
        return render(request, "post/dessert_view.html",
                      context={'dessert_post': dessert_posts})


def dessert_post_details_view(request, post_id):
    if request.method == 'GET':
        dessert_post = Dessert.objects.get(id=post_id)
        return render(request, "post/dessert_details_view.html",
                      context={'dessert_posts': dessert_post})


def category_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, "post/category.html",
                      context={'categories': category})


def category_details_view(request, category_id):
    if request.method == 'GET':
        categories = Category.objects.filter(id=category_id)
        dessert_post = Dessert.objects.filter(category__in=categories)
        return render(request, "post/category_details.html",
                      context={'categories': categories, "dessert_post": dessert_post})
