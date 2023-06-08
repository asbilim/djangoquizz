from django.shortcuts import render

def home(request):

    return render(request, 'listings/index.html')


def login(request):
    
    return render(request,'listings/auth/login.html')