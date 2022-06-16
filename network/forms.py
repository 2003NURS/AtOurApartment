from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class AddPostForm(forms.ModelForm):
#     # def __init__(self,*args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['category'].empty_label = "Таңдаңыз"

#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Registration
#         fields = '__all__'


# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
#     password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class EmailForm(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)


class EmailForm2(forms.Form):
    email = forms.EmailField(label='Пайдаланушы аты')
    subject = forms.CharField(max_length=100)
    # attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)


from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)