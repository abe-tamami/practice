from django.forms import ModelForm
from .models import Fusen

class FusenForm(ModelForm):
    class Meta:
        model = Fusen
        fields = ['title', 'text']
