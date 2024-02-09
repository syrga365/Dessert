"""
URL configuration for dessert project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from post.views import (main_page_view,
                        hello_view,
                        current_date_view,
                        goodbye_view,
                        post_list_view,
                        post_details_view,
                        category_view,
                        category_details_view,
                        post_create_view,
                        category_create_view,
                        review_create_view,
                        post_update_view
                        )
from user.views import register_view, login_view, profile_view, logout_view, veryfy_view, profile_update_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodby/', goodbye_view),
    path('post/', post_list_view, name='list'),
    path('post/<int:post_id>/', post_details_view, name='details'),
    path('post/<int:post_id>/update/', post_update_view, name='post_update'),
    path('category/', category_view, name='category'),
    path('category/<int:category_id>/', category_details_view),
    path('post/create/', post_create_view),
    path('post/<int:post_id>/review/', review_create_view),
    path('category/create_category/', category_create_view),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('verify/', veryfy_view, name='veryfy'),
    path('profile/update_profile/', profile_update_view)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
