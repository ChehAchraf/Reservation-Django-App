from django.shortcuts import render , get_object_or_404
from .models import Activities
# Create your views here.

def home(request):
    all_activities = Activities.objects.all()
    context = {'activity': all_activities}
    return render(request, "home.html", context)

def about(request):
    return render(request, "about.html")

def book_activity(request , activity_id):
    activity = get_object_or_404(Activities,id=activity_id)
    return render(request, 'booking.html', {'activity': activity})