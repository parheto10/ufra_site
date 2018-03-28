from django import forms
from .models import Comment

class EmailForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    to = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'nom',
            'email',
            'contenu',
        ]