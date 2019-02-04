from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .forms import JSErrorForm


def create(request):
    f = JSErrorForm(request.POST)
    if f.is_valid():
        f.save()
        return HttpResponse(status=201)
    else:
        return JsonResponse(f.errors, status=400)
