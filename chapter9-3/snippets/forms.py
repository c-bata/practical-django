from django import forms

from .models import Snippet, Comment


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )

