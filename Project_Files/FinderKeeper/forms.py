from django import forms
from .models import Event

day_choices = ((1, "M"),
               (2, "T"),
               (3, "W"),
               (4, "Th"),
               (5, "F"))

day_dict = {'1': "M",
            '2': "T",
            '3': "W",
            '4': "Th",
            '5': "F"}

class AddEventForm(forms.Form):
    title = forms.CharField(max_length=200, label="Title", widget=forms.TextInput(attrs={'placeholder':'Course number'}))
    days = forms.MultipleChoiceField(choices=day_choices, required=True, widget=forms.CheckboxSelectMultiple())
    startTime = forms.TimeField(required=True)
    endTime = forms.TimeField(required=True)
    location = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)