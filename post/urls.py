from django.urls import path
from post.views import (
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
                        post_update_view,
                        post_delete_view
                        )

urlpatterns = [
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodby/', goodbye_view),
    path('post/', post_list_view, name='list'),
    path('post/<int:post_id>/', post_details_view, name='details'),
    path('post/<int:post_id>/update/', post_update_view, name='post_update'),
    path('post/<int:post_id>/delete/', post_delete_view),
    path('post/<int:post_id>/review/', review_create_view),
    path('post/create/', post_create_view),
    path('category/', category_view, name='category'),
    path('category/<int:category_id>/', category_details_view),
    path('category/create_category/', category_create_view),

]
