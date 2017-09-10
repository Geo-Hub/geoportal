from django.contrib.gis import forms
from .models import *


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            'name_of_sender',
            'email_address',
            'message',
        ]


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            'submitted_from',
            'parcel_no',
        ]
