from django.urls import path

from . imprort views


app_name = "js_error_logger"
urlpatterns = [
    path ('', views.create, name='create'),
]
