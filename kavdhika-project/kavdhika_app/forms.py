from django import forms
from tinymce.widgets import TinyMCE
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write a comment...',
                'rows': 3
            }),
        }
        labels = {
            'content': ''
        } 