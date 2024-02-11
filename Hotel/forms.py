from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import RoomBooking, User, Room


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',  'email', 'password1']

class CustomAuthenticationForm(AuthenticationForm):
    pass

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['roomtype', 'check_in_date', 'check_out_date']

        widgets = {
            'check_in_date': forms.DateInput(attrs={'type':'date'}),
            'check_out_date': forms.DateInput(attrs={'type':'date'}),
            }
    def __init__(self, *args, **kwargs):
        super(RoomBookingForm, self).__init__(*args, **kwargs)
        self.fields['roomtype'].queryset=Room.objects.all()

class BookingSearch(forms.Form):
    booking_code = forms.CharField(max_length=7, label='Booking code')