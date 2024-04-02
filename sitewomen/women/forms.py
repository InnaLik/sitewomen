from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband

class AddPostForm(forms.Form):
    # атрибуты полей формы textinput - это стиль оформления
    title = forms.CharField(max_length=255, min_length=5,
                            label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={'min_length': 'Слишком короткий заголовок',
                                            'required': 'Без заголовка никак'})
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message='Слишком мало символов, минимальный порог 5'),
                               MaxLengthValidator(100)
                           ])
    # поле ввода для текста
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Статус", initial=True)
    # отображение в виде выпадающего списка
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")
    husb = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label="Муж", empty_label="Не замужем")

    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = 'йцукенгшщзхъфывапролджэячсмитьбю0123456789'
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError(message='Должны присутствовать только русские символы, дефис и пробел')
        return title

