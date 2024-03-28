from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    # атрибуты полей формы textinput - это стиль оформления
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-inpur'}))
    slug = forms.SlugField(max_length=255, label='URL')
    # поле ввода для текста
    content = forms.CharField( widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Статус", initial=True)
    # отображение в виде выпадающего списка
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")
    husb = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label="Муж", empty_label="Не замужем")



