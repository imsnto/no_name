from .models import TodoList
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder':'Write your notes here...', 'id':'description', 'name':'description' }),
            'title': forms.TextInput(attrs={'placeholder': 'Write your title here...', 'style':'width:100%;', 'id':'title', 'name':'title'})
        }