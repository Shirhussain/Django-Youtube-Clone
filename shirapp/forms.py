from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        # 'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'comment',
        'name': 'comments',
        'rows': '10'
    }), label='')

    class Meta:
        model = Comment
        fields = ('text', )
