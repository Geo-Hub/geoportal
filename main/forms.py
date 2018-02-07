from django.contrib.gis import forms
from .models import ContactMessage, LandOwner


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage

        fields = [
            'name_of_sender',
            'email_address',
            'message',
        ]


class LandRegistrationForm(forms.ModelForm):
    class Meta:
        model = LandOwner
        fields = [
            'land',
            'first_name',
            'second_name',
        ]
