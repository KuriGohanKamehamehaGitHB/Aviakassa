from django.shortcuts import render
from .models import Flight
import datetime

def flight_list(request):
    today = datetime.date.today()
    flights = Flight.objects.filter(date=today)

    search_from = request.GET.get('from')
    search_to = request.GET.get('to')

    if search_from:
        flights = flights.filter(departure_country__name__icontains=search_from)

    if search_to:
        flights = flights.filter(arrival_country__name__icontains=search_to)

    return render(request, 'index.html', {'flights': flights})
