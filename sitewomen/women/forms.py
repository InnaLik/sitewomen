from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    # атрибуты полей формы
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    # поле ввода для текста
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False)
    # отображение ввиде выпадающего списка
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    husb = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False)
