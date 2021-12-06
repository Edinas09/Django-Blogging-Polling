# polling/urls.py

from django.urls import path
from polling.views import PoolListView, PoolDetailView

urlpatterns = [
    path("", PoolListView.as_view(), name="poll_index"),
    path("polls/<int:pk>/", PoolDetailView.as_view(), name="poll_detail"),
]
