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
                        dessert_posts_view,
                        dessert_post_details_view,
                        category_view,
                        category_details_view
                        )


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_page_view),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodby/', goodbye_view),
    path('dessert_post/', dessert_posts_view),
    path('dessert_post/<int:post_id>/', dessert_post_details_view),
    path('category/', category_view),
    path('category/<int:category_id>/', category_details_view)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
