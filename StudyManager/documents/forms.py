from django import forms
from .models import MIS_Document

# Form to upload documents
class DocForm(forms.ModelForm):
    class Meta:
        # uses the MIS_Document model
        model = MIS_Document
        # set fields in the form -> Important: use a "list" not a "set" to keep the order of the fields
        fields = ['title', 'course', 'pdf', 'author']
        # Set author field to read only, so Users are not able to change the Author field
        widgets = {
            'author': forms.TextInput(attrs={'readonly': 'readonly'}),
        }