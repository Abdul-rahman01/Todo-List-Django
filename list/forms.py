from django import forms
from .models import Todo

INPUT_CLASSES = 'full'


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }