from django.shortcuts import render

# Create your views here.
def home1(request):
    return render(request,'app/home.html')
def show(request):
    return render(request,'app/show.html')
