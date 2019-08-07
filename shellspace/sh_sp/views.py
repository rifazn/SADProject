from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sh_sp/index.html', {})

def upload(request):
    return render(request, 'sh_sp/upload.html', {})

def download(request):
    return render(request, 'sh_sp/download.html', {})
