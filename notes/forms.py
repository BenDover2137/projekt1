from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note

        fields = ['title', 'content','importance']

        fields = ['title', 'content']

