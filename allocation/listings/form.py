from django import forms
from .models import Allocation

class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = '__all__'  # Or specify the fields you want to include in the form
