from django import forms
from post.models import comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['text']
