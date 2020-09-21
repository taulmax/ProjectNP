from django import forms
from .models import *


class PostForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요.'
        },
        max_length=50, label="제목")
    content = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")

    class Meta:
        model = Post
        fields = ['title','content','author',]

class CommentForm(forms.Form):
    content = forms.CharField(
        error_messages={
            'required': '내용을 입력해주세요.'
        },
        widget=forms.Textarea, label="내용")

    class Meta:
        model = Comment
        fields = ['content','author',]
