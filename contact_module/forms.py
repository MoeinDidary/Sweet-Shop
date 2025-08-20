from django import forms
from .models import ContactUs


class ContactUSModleForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ["full_name", 'email', 'title', 'massage']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'massage': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': "massage"
            })
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email'
        }
        error_messages = {
            'full_name': {
                'required': 'Please enter your full name.',
            },
            'email': {
                'required': 'Please enter your email.',
                'invalid': 'Please enter a valid email address.',
            },
            'title': {
                'required': 'Please enter a title.',
            },
            'massage': {
                'required': 'Please enter your message.',
            }
        }
