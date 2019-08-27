from django.shortcuts import render

def index(request):
    context = {
        
    }
    return render(request, 'leap_year/index.html', context)