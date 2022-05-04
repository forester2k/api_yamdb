from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet
from .views import UserViewSet, get_jwt_token, signup

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", signup, name="signup"),
    path("v1/auth/token/", get_jwt_token, name="token"),
]
