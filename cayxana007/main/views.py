from django.shortcuts import render

# Create your views here.
from datetime import date
from django.shortcuts import render
from .models import MenuCategory, Room, SpecialOffer

def home(request):
    return render(request, 'main/home.html')

def menu(request):
    categories = MenuCategory.objects.prefetch_related('items').all()
    return render(request, 'main/menu.html', {'categories': categories})

def reserve_room(request):
    rooms = Room.objects.all()
    return render(request, 'main/reserve_room.html', {'rooms': rooms})

def special_offers(request):
    offers = SpecialOffer.objects.filter(start_date__lte=date.today(), end_date__gte=date.today())
    return render(request, 'main/offers.html', {'offers': offers})
