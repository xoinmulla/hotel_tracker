from django.shortcuts import render, get_object_or_404
from .models import Guest

def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'tracker/guest_list.html', {'guests': guests})

def guest_detail(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    experiences = guest.experiences.all()
    reviews = guest.reviews.all()
    context = {
        'guest': guest,
        'experiences': experiences,
        'reviews': reviews,
    }
    return render(request, 'tracker/guest_detail.html', context)

def home(request):
    return render(request, 'tracker/home.html')
