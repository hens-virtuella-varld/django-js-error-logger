from django.forms import ModelForm
from .models import JSError


class JSErrorForm(ModelForm):
    class Meta:
        model = JSError
        fields = ['name', 'app_id', 'user', 'time', 'url', 'status', 'message', 'stack']
