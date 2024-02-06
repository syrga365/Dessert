from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from post.models import Dessert, Category
from post.form import DessertCreateForm, CategoryCreateForm, ReviewDessertCreateForm
from django.contrib.auth.decorators import login_required


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


@login_required
def dessert_posts_view(request):
    if request.method == "GET":
        dessert_posts = Dessert.objects.all().exclude(user=request.user)
        return render(request, "post/dessert_view.html",
                      context={'dessert_post': dessert_posts})


def dessert_post_details_view(request, post_id):
    if request.method == 'GET':
        form = ReviewDessertCreateForm()
        dessert_post = Dessert.objects.get(id=post_id)
        return render(request, "post/dessert_details_view.html",
                      context={'dessert_posts': dessert_post,
                               'review_form': form})


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


@login_required
def dessert_posts_create_view(request):
    if request.method == 'GET':
        context = {"form": DessertCreateForm()}
        return render(request, 'post/dessert_create.html', context=context)
    elif request.method == 'POST':
        form = DessertCreateForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            # Book.objects.create(**form.cleaned_data)
            form.save()
            return redirect('desserts')
        context = {
            "form": form
        }

        return render(request, 'post/dessert_create.html', context=context)


@login_required
def category_create_view(request):
    if request.method == 'GET':
        context = {"form": CategoryCreateForm()}
        return render(request, 'post/category_create.html', context=context)
    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category')
        context = {
            "form": form
        }
        return render(request, 'post/category_create.html', context=context)


@login_required
def review_dessert_create_view(request, post_id):
    if request.method == 'POST':
        form = ReviewDessertCreateForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.post_id = post_id
            review.user = request.user
            review.save()

        return redirect('dessert_details', post_id=post_id)
