from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def project(request):
    return render(request,'main/Project.html')

def blogs(request):
    return render(request,'main/blog.html')
