from django.shortcuts import render
# This is the main file of Project.
# we make a function in this File.
# Create your views here.
# All request will be here. on Click you get data thats called request.
# Generate response here.

def index(request):
    return render(request,'index.html')
