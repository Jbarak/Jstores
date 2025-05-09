# views.py

from django.shortcuts import render

def homepage(request):
    return render(request, 'base.html')  # or 'yourtemplate.html'
