from django.shortcuts import render,redirect
import requests
from django.core.paginator import Paginator
# Create your views here.
from .models import Image, Data
from .filters import DataFilter


from . import forms
# Create your models here.

def index(request):
    
    return render(request, 'index.html')

def create_image(request):
    if request.method == "POST":
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = forms.ImageForm()
        
    return render(request, 'create_image.html',{'form': form})





def image_list(request):
    images = Image.objects.all()
   
   
    return render(request, 'image_list.html', {'images': images})
 
def create_name(request):
    if request.method == "POST":
        form = forms.DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_name")
            
    else:
        form = forms.DataForm()
        
        
    return render(request, 'create_name.html',{'form': form})

def name_list(request):
    if request.GET and request.GET.get('name'):
        querrySet = Data.objects.all()
        name_filter = DataFilter(request.GET, queryset=querrySet);
        total = name_filter.qs.count()
        
    else:
        name_filter = DataFilter(queryset=Data.objects.none())
        total = 0
    
    return render(request, 'name_list.html', {'filter': name_filter, 'total': total})


def show_names(request):
    names = Data.objects.all()
    return render(request, 'show_all_name.html', {'names': names})
