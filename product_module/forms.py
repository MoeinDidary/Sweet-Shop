from django import forms
from .models import ProductComment


class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your opinion...',
                'class': 'form-control'
            })
        }
