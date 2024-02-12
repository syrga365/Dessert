from django.urls import path
from post.views import (
    # hello_view, current_date_view, goodbye_view, post_list_view, post_details_view, category_view, category_details_view,\
    # post_create_view, category_create_view, review_create_view, post_update_view,post_delete_view \
    main_page_view, HelloView, DateView, GoodByeView,  PostListView, PostDetailView, CategoryView,
    category_details_view, PostCreateView, PostUpdateView, ReviewCreateView, CategoryCreateView, PostDeleteView
)

urlpatterns = [

    path('', main_page_view),
    path('hello2/', HelloView.as_view()),
    path('current_date2/', DateView.as_view()),
    path('goodby2/', GoodByeView.as_view()),
    path('post2/', PostListView.as_view(), name='post_list'),
    path('post2/<int:pk>/', PostDetailView.as_view(), name='details'),
    path('category2/', CategoryView.as_view()),
    path('category2/<int:category_id>/', category_details_view),
    path('post2/create2/', PostCreateView.as_view()),
    path('post2/<int:post_id>/review2/', ReviewCreateView.as_view()),
    path('post2/<int:post_id>/update2/', PostUpdateView.as_view()),
    path('category2/createcategory2/', CategoryCreateView.as_view()),
    path('post2/<int:pk>/delete2/', PostDeleteView.as_view(), name='delete_post'),

    # path('hello/', hello_view),
    # path('current_date/', current_date_view),
    # path('goodby/', goodbye_view),
    # path('post/', post_list_view, name='list'),
    # path('post/<int:post_id>/', post_details_view, name='details'),
    # path('post/<int:post_id>/update/', post_update_view, name='post_update'),
    # path('post/<int:post_id>/delete/', post_delete_view),
    # path('post/<int:post_id>/review/', review_create_view),
    # path('post/create/', post_create_view),
    # path('category/', category_view, name='category'),
    # path('category/<int:category_id>/', category_details_view),
    # path('category/create_category/', category_create_view),

]
