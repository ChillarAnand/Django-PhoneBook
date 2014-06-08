from django import forms
from django.forms.extras.widgets import SelectDateWidget

years = range(1950, 2014)

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required=False)
    phone_no = forms.CharField(max_length=15, required=True) 
    address = forms.CharField(widget=forms.Textarea, required=False)
    
    website = forms.URLField(required=False)
    notes = forms.CharField(widget=forms.TextInput, required=False)
    birthday = forms.DateField(
            widget=SelectDateWidget(years=years), 
            required=False)
    relationship = forms.CharField(max_length=100, required=False)
        
        
class DeleteForm(forms.Form):
    pass
