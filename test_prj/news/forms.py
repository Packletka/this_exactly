from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = [
            'title',
            'anons',
            'news_text',
            'date'
        ]
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи:',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи:',
            }),
            'news_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи:',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата статьи:',
            })
        }
