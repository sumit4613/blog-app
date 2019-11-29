from django.urls import path, include
from .views import PostDetail, PostList
urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post-detail-view'),
    path('', PostList.as_view(), name='post-list-view'),
]
