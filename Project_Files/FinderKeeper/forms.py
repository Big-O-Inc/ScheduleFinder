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
    title = forms.CharField(max_length=200, label="Title", widget=forms.TextInput(attrs={'placeholder':'Course number'}), required=True)
    days = forms.MultipleChoiceField(choices=day_choices, label="Days", required=True, widget=forms.CheckboxSelectMultiple())
    startTime = forms.TimeField(required=True, label="Start",widget=forms.TextInput(attrs={'placeholder':'Enter in military time'}))
    endTime = forms.TimeField(required=True, label="End" ,widget=forms.TextInput(attrs={'placeholder':'Enter in military time'}))
    location = forms.CharField(max_length=200, label="Location",required=False, widget=forms.TextInput(attrs={'placeholder':'ex. 1-101'}))
    description = forms.CharField(label="Description",widget=forms.Textarea, required=False)