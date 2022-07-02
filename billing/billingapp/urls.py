from rest_framework import routers
from .views import OrganizationViewSet, BillsViewSet

router = routers.DefaultRouter()
# router.register('clients', ClientViewSet, basename='client')
router.register(
    'organizations',
    OrganizationViewSet,
    basename='organization'
    )
router.register('bills', BillsViewSet, basename='bills')

urlpatterns = router.urls
