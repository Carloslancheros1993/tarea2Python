from rest_framework.routers import DefaultRouter

from empleados.views import EmpleadoViewSet

router = DefaultRouter()
router.register('', EmpleadoViewSet)

urlpatterns = router.urls