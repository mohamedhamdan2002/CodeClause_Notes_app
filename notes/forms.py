from django import forms
from .models import Notes
class Notesfrom(forms.ModelForm):
    class Meta:
        model=Notes
        fields=[
            'title',
            'notes',
        ]