from rest_framework.routers import DefaultRouter

from permisos.views import PermisoViewSet

router = DefaultRouter()
router.register('', PermisoViewSet)

urlpatterns = router.urls