from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from post.models import Dessert, Category
from post.form import CategoryForm, PostCreateForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


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


def post_list_view(request):
    if request.method == "GET":
        search = request.GET.get('search', '')
        sort = request.GET.get('sort', 'title')
        category = request.GET.get('category', '')
        page = request.GET.get('page', 1)
        posts = Dessert.objects.all().exclude(user=request.user)
        if search:
            posts = posts.filter(
                Q(title__contains=search) | Q(content__contains=search)
            )
        if sort:
            posts = posts.order_by(sort)
        if category:
            posts = posts.filter(category__id=category)

        limit = 2
        max_pages = posts.__len__() / limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (int(page) - 1) * limit
        end = start + limit

        posts = posts[start:end]

        category = Category.objects.all()
        context = {'posts': posts, 'categories': category, 'max_pages': range(1, max_pages + 1)}
        return render(request, "post/list.html",
                      context=context)


def post_details_view(request, post_id):
    form = ReviewForm()
    if request.method == 'GET':
        posts = Dessert.objects.get(id=post_id)
        has_change_permission = posts.user == request.user
        context = {'posts': posts, 'review_form': form, 'has_change_permission': has_change_permission}
        return render(request, "post/details.html",
                      context=context)


def category_view(request):
    if request.method == "GET":
        category = Category.objects.all()
        return render(request, "post/category.html",
                      context={'categories': category})


def category_details_view(request, category_id):
    if request.method == 'GET':
        categories = Category.objects.filter(id=category_id)
        posts = Dessert.objects.filter(category__in=categories)
        return render(request, "post/category_details.html",
                      context={'categories': categories, "posts": posts})


@login_required
def post_create_view(request):
    if request.method == 'GET':
        context = {"form": PostCreateForm()}
        return render(request, 'post/create.html', context=context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('list')
        context = {
            "form": form
        }

        return render(request, 'post/create.html', context=context)


@login_required
def post_update_view(request, post_id):
    try:
        posts = Dessert.objects.get(id=post_id)
    except Dessert.DoesNotExist:
        return HttpResponse('None')
    if posts.user != request.user:
        return HttpResponse('Permission denied', status=403)
    if request.method == 'GET':
        form = PostCreateForm(instance=posts)
        return render(request, 'post/update.html', {'form': form})
    elif request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('details', post_id=post_id)
        return render(request, 'post/update.html', {'form': form})


@login_required
def category_create_view(request):
    if request.method == 'GET':
        context = {"form": CategoryForm()}
        return render(request, 'post/category_create.html', context=context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category')
        context = {
            "form": form
        }
        return render(request, 'post/category_create.html', context=context)


@login_required
def review_create_view(request, post_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.posts_id = post_id
            review.user = request.user
            review.save()

        return redirect('details', post_id=post_id)


@login_required
def post_delete_view(request, post_id):
    try:
        posts = Dessert.objects.get(id=post_id)
    except Dessert.DoesNotExist:
        return HttpResponse('None')
    if posts.user != request.user:
        return HttpResponse('Permission denied', status=403)
    posts.delete()
    return redirect('list')
