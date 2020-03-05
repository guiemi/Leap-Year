from django.shortcuts import render, redirect, get_object_or_404
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
        new_year = LeapYear(year=request.POST['year'])
        new_year.save()

    return redirect("index")

def deleteYear(request, year_id):
    years = get_object_or_404(LeapYear, pk=year_id)
    years.delete()
    return redirect("index")



# def calculate(request, year_id):
#     year_id = LeapYear.objects.get(pk=year_id)
#     # is_leap = LeapYear.objects.order_by("id")
    
#     if year_id > 2000:
#         year_id.is_leap = True
#         year_id.save()
#     return print(f"year_id: {year_id}")