import flights
from django.shortcuts import render
from .models import Airport, Flight, Pessenger
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
    
def flight(request,flight_id):
    flight = Flight.objects.get(pk=flight_id) 
    return render(request, "flights/flights.html", {
        "flight": flight,
        "pessengers": flight.pessengers.all(),
        "non_pessengers": Pessenger.objects.exclude(flights=flight).all()
    })
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        pessenger = Pessenger.objects.get(pk=int(request.POST['pessenger']))
        pessenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
