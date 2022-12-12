from django import forms
class section(forms.Form):
    Title = forms.CharField(label='Оглавление')
    URL = forms.URLField(label='Ccылка')
    img= forms.ImageField(label='Картинка')
    text = forms.CharField(label='Напишите текст статьи',widget=forms.Textarea)
    Publish = forms.CharField(label='Опубликовать?',widget=forms.CheckboxInput)
    Category = forms.ChoiceField(label='Категория',choices=((1, 'Выберите категорию'), (2, 'Свежие'), (3, 'Старые')))
    data = forms.DateField(label='Дата публикации')