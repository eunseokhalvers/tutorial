from django.forms import ModelForm
from django import forms
from models import Home, Service, Recruit, Contact


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'email', 'phone']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']