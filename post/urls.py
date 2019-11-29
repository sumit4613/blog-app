from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from .views import (PostDetail, PostList, PostViewSet, UserDetail, UserList,
                    UserViewSet)

router = SimpleRouter()
router.register("users", UserViewSet, base_name="users")
router.register("", PostViewSet, base_name="posts")

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post-detail-view"),
    path("", PostList.as_view(), name="post-list-view"),
    path("users/", UserList.as_view(), name="user-list-view"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user-detail-view"),
    re_path(r"v2/", include((router.urls, "post"), namespace="viewset-urls")),
]
