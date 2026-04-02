from django.shortcuts import render

rooms = [
    {"id":1, "name": "Let's Learn Python"},
    {"id":2, "name": "Design WIth Me"},
    {"id":3, "name": "Frontend Developers"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')