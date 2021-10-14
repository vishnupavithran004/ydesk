from django.urls import path, include
from .views import OrganizationViewSet, AccountViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'organization', OrganizationViewSet, 
    basename='organization')
router.register(r'account', AccountViewSet, 
    basename='account')

urlpatterns = [
    path('', include(router.urls)),
]