from django.shortcuts import render

def showDemoPage(request):
    return render(request, 'demo.html')

def showLoginPage(request):
    return render(request, 'login.html')

