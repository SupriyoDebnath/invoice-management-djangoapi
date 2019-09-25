from rest_framework import routers
from .viewsets import UserViewset

# Create your routers here.
router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewset, basename='users')

urlpatterns = router.urls