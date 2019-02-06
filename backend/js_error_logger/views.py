from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .forms import JSErrorForm
from .models import JSError
from .serializers import JSErrorSerializer


class JSErrorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = JSError.objects.all()
    serializer_class = JSErrorSerializer


def create(request):
    f = JSErrorForm(request.POST)
    if f.is_valid():
        f.save()
        return HttpResponse(status=201)
    else:
        return JsonResponse(f.errors, status=400)
