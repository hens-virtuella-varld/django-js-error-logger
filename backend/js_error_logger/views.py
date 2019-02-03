from django.shortcuts import render
from .forms import JSErrorForm


def create(request):
    f = JSErrorForm(request.POST)
    f.save()
