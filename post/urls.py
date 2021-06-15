from django.urls import path

from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


app_name = 'post'
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls