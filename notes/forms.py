from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
<<<<<<< HEAD
        fields = ['title', 'content','importance']
=======
        fields = ['title', 'content']
>>>>>>> bcd463fa155895d281d17e13cb33b5f89f695e4f
