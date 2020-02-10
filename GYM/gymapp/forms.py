from django import forms
from django.forms import ModelForm
from .models import Gym
from gymapp.models import Trainer, Members, abc, Payment, Contat


class GymCreate(forms.ModelForm):
    class Meta:
        model = Gym
        fields = '__all__'


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        

class AbcForm(forms.ModelForm):
    class Meta:
        model = abc
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class ContatForm(forms.ModelForm):
    class Meta:
        model = Contat
        fields = '__all__'








