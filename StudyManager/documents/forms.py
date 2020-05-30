from django import forms
from .models import MIS_Document

class DocForm(forms.ModelForm):
    class Meta:
        model = MIS_Document
        fields = {'title', 'course', 'pdf', 'author'}

        # Set field to read only, so Users are not able to change the Author field
        widgets = {
            'author': forms.TextInput(attrs={'readonly': 'readonly'}),
        }