from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Month, Day, Country, Holiday


@deconstructible
class DescriptionValidator:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, value, *args, **kwargs):
        if 'бебе' in value:
            raise ValidationError(message='Недопустим флуд')
        return value


class AddFormsHoliday(forms.ModelForm):
    month = forms.ModelChoiceField(queryset=Month.objects.all(), empty_label='Не выбрано', label='Месяц')
    day = forms.ModelChoiceField(queryset=Day.objects.all(), empty_label='Не выбрано', label='День')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Не выбрано', label='Страна')

    class Meta:
        model = Holiday
        fields = ['name', 'slug', 'international', 'worldwide', 'ordinary_holiday', 'description_holi', 'file']
        widgets = {'description_holi': forms.Textarea(attrs={'cols': 50, 'rows': 5})}

        labels = {'description_holi': 'Описание праздника'}

    def clean_name(self):
        value = self.cleaned_data['name']
        if '_' in value:
            raise ValidationError(message='Символ подчеркивания недопустим')
        return value


class AddFileUpload(forms.Form):
    file = forms.FileField(label='Файл:')
