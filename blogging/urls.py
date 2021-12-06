# blogging/urls.py

from django.urls import path
from blogging.views import BlogListView, BlogDetailView, stub_view


# from blogging.views import stub_view

urlpatterns = [
    path("", BlogListView.as_view(), name="post_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
]

# urlpatterns = [
#     path('', stub_view, name="blog_index"),
#     path('posts/<int:post_id>/', stub_view, name="blog_detail"),
# ]
