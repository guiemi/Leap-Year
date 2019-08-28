from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from leap_year.models import LeapYear
from leap_year.forms import LeapYearForm


def index(request):
    years = LeapYear.objects.order_by("id")
    
    form = LeapYearForm()

    context = {
        'years': years,
        'form': form,
    }
    return render(request, 'leap_year/index.html', context)

@require_POST
def addYear(request):
    form = LeapYearForm(request.POST)

    print(request.POST['year'])
    
    if form.is_valid():
        new_year = LeapYear(number=request.POST['text'])
        # new_year = LeapYear(=request.POST['text'])
        new_year.save()


    return redirect("index")
