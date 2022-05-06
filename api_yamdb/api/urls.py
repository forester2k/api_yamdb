from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,
                    GenreViewSet,
                    TitleViewSet,
                    ReviewViewSet,
                    CommentViewSet)
from .views import UserViewSet, get_jwt_token, signup

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register('titles', TitleViewSet)
router.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename='review',
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename='comment',
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", signup, name="signup"),
    path("v1/auth/token/", get_jwt_token, name="token"),
]
