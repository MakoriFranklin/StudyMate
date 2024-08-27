from django.shortcuts import render

from .models import Room

rooms = [
    {'id':1, 'name': 'Lets learn python'},
    {'id':2, 'name': 'Lets learn Node js'},
    {'id':3, 'name': 'Lets learn c#'},
    {'id':4, 'name': 'Lets learn Java'},
]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

# Create your views here.
