from django import forms
from django.forms import fields

from .models import Post, Body

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        labels = {'text':''}

class BodyForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = ['text']
        labels = {'text': 'body:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

