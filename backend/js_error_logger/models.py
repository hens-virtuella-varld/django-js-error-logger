from django.db import models


class JSError(models.Model):
    name = models.CharField(max_length=200)
    app_id = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    time = models.DateTimeField()
    url = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    stack = models.TextField(max_length=2000)

