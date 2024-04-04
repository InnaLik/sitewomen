from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from .models import Month, Day, Country


class DescriptionValidator:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, value, *args, **kwargs):
        if 'бебе' in value:
            raise ValidationError(message='Недопустим флуд')
        return value

class AddFormsHoliday(forms.Form):
    name = forms.CharField(max_length=255, label='Наименование праздника', validators=
    [MinLengthValidator(10, message='Минимально должно быть 10 символов')])
    slug = forms.CharField(max_length=255, label='url')
    international = forms.BooleanField(required=False, label='Статус международного')
    worldwide = forms.BooleanField(required=False, label='Статус Всемирного')
    ordinary_holiday = forms.BooleanField(label='Статус одной страны', required=False)
    month = forms.ModelChoiceField(queryset=Month.objects.all(), empty_label='Не выбрано', label='Месяц')
    day = forms.ModelChoiceField(queryset=Day.objects.all(), empty_label='Не выбрано', label='День')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label='Не выбрано', label='Страна')
    description_holi = forms.CharField(widget=forms.Textarea(attrs={"cols": "40", "rows": "5"}), label='Описание и история праздника',
                                       validators=[DescriptionValidator()])

    # email = forms.EmailField(label='Ваш email')


    def clean_name(self):
        value = self.cleaned_data['name']
        if '_' in value:
            raise ValidationError(message='Символ подчеркивания недопустим')
        return value

