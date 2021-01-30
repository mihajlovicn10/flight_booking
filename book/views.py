from datetime import datetime
from django.shortcuts import render, redirect
from book.models import Flight, Booking

# Create your views here.

#DOMACi
# unutar booking list stavi dugme da se korisnik vrati  na dodavanje bookinga

#DOMACI2
#rasclani templatove napravi base.html i ostali da nasledjuju taj html


def index_view(request):
    return redirect('/booking')


def booking_list(request):
    """
        ako je get zahtev prikazaće html formu za listu bukinga
        na putanji booking_list
    """
    user = request.user
    bookings = Booking.objects.filter(user = user).all()
    return render(request,"booking_list.html", {"bookings":bookings})


def delete_booking(request, pk): 
    booking = Booking.objects.get(pk = pk)
    booking.delete()
    return redirect("/booking")

def booking_view(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST' and request.POST['command'] != "book":
        flight = None
        try:
            flight = Flight.objects.get(from_city=request.POST['from_city'].strip(), to_city=request.POST['to_city'].strip(), departing__date=datetime.strptime(request.POST['departing'], "%Y-%m-%d"))
            return render(request, 'booking.html', {"available":True, "flight":flight})
        except Flight.DoesNotExist:
            return render(request, 'booking.html', {"available":False})



    if request.method == 'POST' and request.POST['command']=="book":
        user = request.user
        flight_id = int(request.POST["flight_id"])
        flight = Flight.objects.get(pk=flight_id)
        booking = Booking.objects.filter(user=user, flight=flight).first()
        if booking:
            return render(request, 'booking.html', {"booking":"Booking for this flight already exists!"})
        booking = Booking(user=user, flight=flight)
        booking.save()
        return render(request, 'booking.html', {"booking":"Booking successful!"})
    else:
        return render(request, 'booking.html')