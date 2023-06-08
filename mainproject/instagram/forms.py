from django import forms
from .models import ContentModel


class ContentForm(forms.ModelForm):
    class Meta:
        model=ContentModel
        fields='__all__'