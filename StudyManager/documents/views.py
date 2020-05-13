from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import DocForm
from .models import ISD_Document

# Create your views here.

def doclist(request):
    doc = ISD_Document.objects.all()

    return render(request, 'documents/documents.html', {
        'Document': doc
    })

def upload(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/documents/')
    else:
        form = DocForm()
    return render(request, 'documents/upload.html', {
        'form': form
    })

#Delete document and go back to the documents overview
def deletedoc(request, pk):
    if request.method == 'POST':
        doc = ISD_Document.objects.get(pk=pk)
        doc.delete()
    return redirect('/documents/')


