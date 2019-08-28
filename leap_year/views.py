from django.shortcuts import render
from leap_year.models import LeapYear


def index(request):
    years = LeapYear.objects.order_by("id")

    context = {
        'years': years,
    }
    return render(request, 'leap_year/index.html', context)

def after_century(request):
    is_leap = LeapYear.objects.order_by("id")

    context = {
        'is_leap': is_leap,
    }

    return render(request, 'leap_year/index.html', context)
