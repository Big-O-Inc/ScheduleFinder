from django import forms
from .models import Event
from bootstrap_modal_forms.forms import BSModalModelForm

day_choices = ((1, "Monday"),
               (2, "Tuesday"),
               (3, "Wednesday"),
               (4, "Thursday"),
               (5, "Friday"))

class AddEventForm(forms.Form):
    title = forms.CharField(max_length=200)
    days = forms.MultipleChoiceField(choices=day_choices, required=True, widget=forms.CheckboxSelectMultiple())
    startTime = forms.TimeField(required=True)
    endTime = forms.TimeField(required=True)
    location = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)