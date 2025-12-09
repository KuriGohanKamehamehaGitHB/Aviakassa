from django.shortcuts import render
from .models import Flight
import datetime

def flight_list(request):
    # Получаем сегодняшнюю дату
    today = datetime.date.today()
    
    # Изначально берем ТОЛЬКО перелеты на сегодня
    flights = Flight.objects.filter(date=today)

    # Получаем данные из GET-запроса (то, что ввел пользователь)
    search_from = request.GET.get('from')
    search_to = request.GET.get('to')

    # Если пользователь ввел страну вылета
    if search_from:
        # __icontains ищет частичное совпадение без учета регистра
        flights = flights.filter(departure_country_name_icontains=search_from)
    
    # Если пользователь ввел страну прилета
    if search_to:
        flights = flights.filter(arrival_country_name_icontains=search_to)

    return render(request, 'index.html', {'flights': flights})