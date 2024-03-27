from django import forms
from .models import Month, Day, Country


class AddFormsHoliday(forms.Form):
    name = forms.CharField(max_length=255)
    slug = forms.CharField(max_length=255)
    international = forms.BooleanField(required=False)
    worldwide = forms.BooleanField(required=False)
    ordinary_holiday = forms.BooleanField()
    month = forms.ModelChoiceField(queryset=Month.objects.all())
    day = forms.ModelChoiceField(queryset=Day.objects.all())
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    description_holi = forms.CharField(widget=forms.Textarea())