from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import DocForm
from .models import MIS_Document
from django.http import HttpResponseRedirect

# View that handles the document upload -> Only allows / saves file if POST method is used, otherwise ignore it
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

# Delete document and go back to the documents overview
def deletedoc(request, pk):
    if request.method == 'POST':
        doc = MIS_Document.objects.get(pk=pk)
        doc.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
# View to display the MIS_Document model -> Show all Documents
def doclist(request):
    doc = MIS_Document.objects.all()
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Information Systems Development" Documents
def ISDdocs(request):
    doc = MIS_Document.objects.filter(course='ISD')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Enterprise Architecture Management" Documents
def EAMdocs(request):
    doc = MIS_Document.objects.filter(course='EAM')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Management Information Systems" Documents
def MISdocs(request):
    doc = MIS_Document.objects.filter(course='MIS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Business Process Management" Documents
def BPMdocs(request):
    doc = MIS_Document.objects.filter(course='BPM')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Data and Application Security" Documents
def DASdocs(request):
    doc = MIS_Document.objects.filter(course='DAS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Data Management" Documents
def DMdocs(request):
    doc = MIS_Document.objects.filter(course='DM')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Business Statistics" Documents
def BSdocs(request):
    doc = MIS_Document.objects.filter(course='BS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Innovation Lab" Documents
def ILdocs(request):
    doc = MIS_Document.objects.filter(course='IL')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Information Systems Modelling" Documents
def ISMdocs(request):
    doc = MIS_Document.objects.filter(course='ISM')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Digital Innovation" Documents
def DIdocs(request):
    doc = MIS_Document.objects.filter(course='DI')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Data Science" Documents
def DSdocs(request):
    doc = MIS_Document.objects.filter(course='DS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Digital Business" Documents
def DBdocs(request):
    doc = MIS_Document.objects.filter(course='DB')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Emerging IT Topics" Documents
def EITdocs(request):
    doc = MIS_Document.objects.filter(course='EIT')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Human Centered Design" Documents
def HCDdocs(request):
    doc = MIS_Document.objects.filter(course='HCD')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Research Methods" Documents
def RMdocs(request):
    doc = MIS_Document.objects.filter(course='RM')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Research Seminar" Documents
def RSdocs(request):
    doc = MIS_Document.objects.filter(course='RS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Project Seminar" Documents
def PSdocs(request):
    doc = MIS_Document.objects.filter(course='PS')
    return render(request, 'documents/documents.html', {'Document': doc})

# View to display the MIS_Document model -> Show only "Master Thesis" Documents
def MTdocs(request):
    doc = MIS_Document.objects.filter(course='MT')
    return render(request, 'documents/documents.html', {'Document': doc})

