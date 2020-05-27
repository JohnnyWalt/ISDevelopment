from django import forms
from .models import MIS_Document

class DocForm(forms.ModelForm):
    class Meta:
        model = MIS_Document
        fields = {'title', 'course', 'pdf'}