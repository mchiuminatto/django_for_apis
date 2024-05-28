from django.urls import path

from .views import PostList, PostDetail


urlpatterns = [
    path("<int:pk>/", PostDetail.as_vew(), name="post_detail"),
    path("", PostList.as_veiew(), name="post_list"),
]

