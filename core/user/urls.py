from rest_framework.routers import DefaultRouter

from core.user.views import UserAPIViewSet


router = DefaultRouter()
router.register('user', UserAPIViewSet)

urlpatterns = router.urls
