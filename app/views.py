from django.shortcuts import render

# Create your views here.
def forms(request):
    return render(request,'forms.html')

def tables(request):
    return render(request,'tables.html')
def groupselector(request):
    return render(request,'groupselector.html')
def pseudoselector(request):
    return render(request,'pseudoselector.html')

def idselector(request):
    return render(request,'idselector.html')

def classselector(request):
    return render(request,'classselector.html')

def adjacentselector(request):
    return render(request,'adjacentselector.html')
def internalstyles(request):
    return render(request,'internalstyles.html')

def animation(request):
    return render(request,'animation.html')

def image(request):
    return render(request,'image.html')

def externalstyle(request):
    return render(request,'externalstyle.html')
