from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.template import loader
from django.http import HttpResponse
from .models import Room, RoomBooking
from .forms import  CustomUserCreationForm, CustomAuthenticationForm, RoomBookingForm, BookingSearch


# Create your views here.
def Home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def Rooms(request):
    rooms = Room.objects.all()
    template = loader.get_template('rooms.html')
    context = {'rooms':rooms}
    return HttpResponse(template.render(context, request))

def Registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Login')
    else:
        form = CustomUserCreationForm()
    template = loader.get_template('registration.html')
    context = {'form': CustomUserCreationForm(),}
    return HttpResponse(template.render(context, request))

def Login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('booking')
    else:
        form = CustomAuthenticationForm()
    template = loader.get_template('login.html')
    context = {'login': CustomAuthenticationForm(),}
    return HttpResponse(template.render(context, request))

@login_required
def BookRoom(request):
    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            room_booking = form.save(commit=False)
            room_booking.user = request.user
            room_booking.save()
            return redirect('booking_success', booking_code=room_booking.booking_code)
    else:
        form = RoomBookingForm()
    template = loader.get_template('booking.html')
    context = {'booking': RoomBookingForm()}
    return HttpResponse(template.render(context, request))

@login_required
def search_booking(request):
    if request.method == 'POST':
        form = BookingSearch(request.POST)
        if form.is_valid():
            booking_code = form.cleaned_data['booking_code']
            booking = get_object_or_404(RoomBooking, booking_code=booking_code)
            return render(request, 'booking_detail.html', {'booking': booking})
    else:
        form = BookingSearch()
    template = loader.get_template('booking_search.html')
    context = {'form': BookingSearch()}
    return HttpResponse(template.render(context, request))

@login_required
def booking_success(request, booking_code):
    template = loader.get_template('success.html')
    context = {'booking_code':booking_code}
    return HttpResponse(template.render(context, request))