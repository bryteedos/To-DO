from dataclasses import fields
from django import forms
from.models import tasklist
from todolistapp import models

class taskform(forms.ModelForm):
    class Meta:
        model=tasklist
        fields=['task', 'status']