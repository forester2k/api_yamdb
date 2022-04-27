from rest_framework.routers import DefaultRouter

from .views import TitleViewSet

router_v1 = DefaultRouter()
router_v1.register(r"titles", TitleViewSet, basename='titles')
