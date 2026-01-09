from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
def index(request):
    return render(request, 'blog/index.html')
# Create your views here.
def blog(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries' : entries} # Store the data in "context" dictionaries
    return render(request, 'blog/blog.html', context)
def add(request):
    form = EntryForm()
    context = {'form' : form} # Pass the form to template
    return render(request, 'blog/add.html', context)
