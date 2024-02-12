from typing import Any
from datetime import datetime

from django.views import View
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404

from post.models import Dessert, Category, ReviewDessert
from post.form import CategoryForm, PostCreateForm, ReviewForm


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, It's my project!")


class DateView(View):
    def get(self, request):
        current_datetime = datetime.now()
        return HttpResponse(current_datetime)


class GoodByeView(View):
    def get(self, request):
        return HttpResponse('Good bye, user!!!')


class PostListView(ListView):
    model = Dessert
    template_name = 'post/list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset().exclude(user=self.request.user)

        search = self.request.GET.get('search', '')
        sort_by_created_at = self.request.GET.get('sort', 'created_at')
        sort_by_title = self.request.GET.get('sort', 'title')
        category = self.request.GET.get('category', '')

        if search:
            queryset = queryset.filter(
                Q(title__contains=search) | Q(content__contains=search)
            )
        if sort_by_created_at:
            queryset = queryset.order_by(sort_by_created_at)
        if sort_by_title:
            queryset = queryset.order_by(sort_by_title)
        if category:
            queryset = queryset.filter(category__id=category)
        return queryset


class PostDetailView(DetailView):
    model = Dessert
    context_object_name = 'posts'
    template_name = 'post/details.html'

    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['has_change_permission'] = (context['posts'].user == self.request.user)
        return context


class CategoryView(ListView):
    model = Category
    template_name = 'post/category.html'
    context_object_name = 'categories'


class CategoryDetailsView(ListView):
    template_name = "post/category_details.html"
    context_object_name = "posts"
    queryset = Dessert.objects.all()

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return self.queryset.filter(category=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        categories = Category.objects.filter(id=category_id)
        context['categories'] = categories
        return context


class PostCreateView(CreateView):
    model = Dessert
    form_class = PostCreateForm
    template_name = 'post/create.html'
    success_url = '/post2/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated:
            return reverse('post_list')
        return reverse('login')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Dessert
    form_class = PostCreateForm
    pk_url_kwarg = 'post_id'
    template_name = 'post/update.html'
    success_url = '/post2/'

    def get(self, request, *args, **kwargs):
        posts = self.get_object()
        if posts.user != request.user:
            return HttpResponse('Permission denied', status=403)
        return super().get(request, *args, **kwargs)


#
class ReviewCreateView(CreateView):
    model = ReviewDessert
    form_class = ReviewForm
    pk_url_kwarg = 'post_id'
    template_name = 'post/details.html'

    def get_success_url(self):
        return reverse('details', kwargs={'pk': self.kwargs['post_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get(self.pk_url_kwarg)
        context['post_id'] = post_id
        return context

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.instance.post_id = self.kwargs.get(self.pk_url_kwarg)
        return super().form_valid(form)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'post/category_create.html'
    success_url = '/category2/'


class PostDeleteView(DeleteView):
    model = Dessert
    context_object_name = 'posts'
    template_name = 'post/delete.html'
    success_url = '/profile/'

    def get(self, request, *args, **kwargs):
        posts = self.get_object()
        if posts.user != request.user:
            return HttpResponse('Permission denied', status=403)
        # posts.delete()
        return super().get(request, *args, **kwargs)

# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello, It's my project")
#
#
# def current_date_view(request):
#     if request.method == 'GET':
#         current_datetime = datetime.now()
#         return HttpResponse(current_datetime)
#
#
# def goodbye_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Good bye, user!!!")
#
#
# def post_list_view(request):
#     if request.method == "GET":
#         search = request.GET.get('search', '')
#         sort = request.GET.get('sort', 'title')
#         category = request.GET.get('category', '')
#         page = request.GET.get('page', 1)
#         posts = Dessert.objects.all().exclude(user=request.user)
#         if search:
#             posts = posts.filter(
#                 Q(title__contains=search) | Q(content__contains=search)
#             )
#         if sort:
#             posts = posts.order_by(sort)
#         if category:
#             posts = posts.filter(category__id=category)
#
#         limit = 2
#         max_pages = posts.__len__() / limit
#         if round(max_pages) < max_pages:
#             max_pages = round(max_pages) + 1
#         else:
#             max_pages = round(max_pages)
#
#         start = (int(page) - 1) * limit
#         end = start + limit
#
#         posts = posts[start:end]
#
#         category = Category.objects.all()
#         context = {'posts': posts, 'categories': category, 'max_pages': range(1, max_pages + 1)}
#         return render(request, "post/list.html",
#                       context=context)
#
#
# def post_details_view(request, post_id):
#     form = ReviewForm()
#     if request.method == 'GET':
#         posts = Dessert.objects.get(id=post_id)
#         has_change_permission = posts.user == request.user
#         context = {'posts': posts, 'review_form': form, 'has_change_permission': has_change_permission}
#         return render(request, "post/details.html",
#                       context=context)
#
#
# def category_view(request):
#     if request.method == "GET":
#         category = Category.objects.all()
#         return render(request, "post/category.html",
#                       context={'categories': category})
#
#
# def category_details_view(request, category_id):
#     if request.method == 'GET':
#         categories = Category.objects.filter(id=category_id)
#         posts = Dessert.objects.filter(category__in=categories)
#         return render(request, "post/category_details.html",
#                       context={'categories': categories, "posts": posts})
#
#
# @login_required
# def post_create_view(request):
#     if request.method == 'GET':
#         context = {"form": PostCreateForm()}
#         return render(request, 'post/create.html', context=context)
#     elif request.method == 'POST':
#         form = PostCreateForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('list')
#         context = {
#             "form": form
#         }
#
#         return render(request, 'post/create.html', context=context)
#
#
# @login_required
# def post_update_view(request, post_id):
#     try:
#         posts = Dessert.objects.get(id=post_id)
#     except Dessert.DoesNotExist:
#         return HttpResponse('None')
#     if posts.user != request.user:
#         return HttpResponse('Permission denied', status=403)
#     if request.method == 'GET':
#         form = PostCreateForm(instance=posts)
#         return render(request, 'post/update.html', {'form': form})
#     elif request.method == "POST":
#         form = PostCreateForm(request.POST, request.FILES, instance=posts)
#         if form.is_valid():
#             form.save()
#             return redirect('details', post_id=post_id)
#         return render(request, 'post/update.html', {'form': form})
#
#
# @login_required
# def category_create_view(request):
#     if request.method == 'GET':
#         context = {"form": CategoryForm()}
#         return render(request, 'post/category_create.html', context=context)
#     elif request.method == 'POST':
#         form = CategoryForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('category')
#         context = {
#             "form": form
#         }
#         return render(request, 'post/category_create.html', context=context)
#
#
# @login_required
# def review_create_view(request, post_id):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.posts_id = post_id
#             review.user = request.user
#             review.save()
#
#         return redirect('details', post_id=post_id)
#
#
# @login_required
# def post_delete_view(request, post_id):
#     try:
#         posts = Dessert.objects.get(id=post_id)
#     except Dessert.DoesNotExist:
#         return HttpResponse('None')
#     if posts.user != request.user:
#         return HttpResponse('Permission denied', status=403)
#     posts.delete()
#     return redirect('list')
