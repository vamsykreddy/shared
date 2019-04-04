from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from app.forms import DocumentForm
from app.models import Document

# Create your views here.
#class Home(TemplateView):
#    template_name = 'index.html'

def Home(request):
    return render(request,'index.html')

def Upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<html><body>Upload successfull</body></html>')
    else:
        form = DocumentForm()
    return render(request,'upload.html',{'form':form})