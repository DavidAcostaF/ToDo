from django import forms

from apps.todo.models import ToDo

class formTodo(forms.Form):
    class Meta:
        model = ToDo
        fields = ['todo']
        widgets = {
            'todo': forms.CharField()
        }
