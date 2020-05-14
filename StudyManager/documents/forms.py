from django import forms
from .models import ISD_Document

class DocForm(forms.ModelForm):
    class Meta:
        model = ISD_Document
        fields = {'title', 'pdf'}