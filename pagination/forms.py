from django import forms
from django.db import models

from .models import Image, Data


class ImageForm(forms.ModelForm):
  
  class Meta:
    model = Image
    fields = ['image']
    labels = {
        'image': 'Image'
    }
    
    
    
    
class DataForm(forms.ModelForm):
  
  class Meta:
    model = Data
    fields = ['name']
    labels = {
        'name': 'Name'
    }
    widgets = {
        'name': forms.TextInput(attrs={
            "class": "w-full px-4 py-2 border border-gray-300 rounded-lg \
                      focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Enter name"
        })
    }
    
    
    