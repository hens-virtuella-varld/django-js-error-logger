from django.urls import path

from . import views


app_name = "js_error_logger"
urlpatterns = [
    path ('', views.create, name='create'),
]
