#duplicate of boooking
from django import forms
from . models import Booking

class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        #model of which duplicate is required
        model=Booking
        #which are the fields required
        fields='__all__'
        #to get date picker widget in form
        widgets={
            'booking_date':DateInput(),
        }
        #to set labels name in the booking form
        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",
        }