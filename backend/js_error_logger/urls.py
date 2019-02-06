from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'js_error', views.JSErrorViewSet)

app_name = "js_error_logger"
urlpatterns = [
    path('', include(router.urls)),
]
