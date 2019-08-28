from django.shortcuts import render
from leap_year.models import LeapYear


def index(request):
    years = LeapYear.objects.order_by("id")

    context = {
        'years': years,
    }
    return render(request, 'leap_year/index.html', context)


