from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.urls import reverse_lazy
from .forms import DocumentForm
from .models import Document
# from django.core.files import UploadedFiles
# Create your views here.


def form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print('details of file', request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.save()
            return render(request, 'home.html', {'result': 'File Uploaded successfully'})
            # render(request, 'home.html')
        else:
            return render(request,'document_form_upload.html', {'form': form})
    else:
        form = DocumentForm()
        print(form)
        return render(request, 'document_form_upload.html', {'form': form})

#
# def home(request):


def home(request):
    doc = Document.objects.all()
    render(request, 'home.html')
