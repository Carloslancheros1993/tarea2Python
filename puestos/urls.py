from rest_framework.routers import DefaultRouter

from puestos.views import PuestoViewSet

router = DefaultRouter()
router.register('', PuestoViewSet)

urlpatterns = router.urls