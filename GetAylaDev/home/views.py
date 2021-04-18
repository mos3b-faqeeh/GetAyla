from django.shortcuts import render

# Create your views here.



def services (request):
    return render(request, 'services.html', {})



def home (request):
    return render(request, 'home.html', {})