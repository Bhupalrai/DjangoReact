from django.conf.urls import include
from django.urls import path
from . import views
from rest_framework import routers

from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', views.first),
    path('api/', include(router.urls))
]
