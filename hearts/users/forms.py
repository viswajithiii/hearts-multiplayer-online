from django import forms
from users.models import userprofile
from django.contrib.auth.models import User

class AddUserForm(forms.Form):

    username = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    password = forms.CharField(min_length = 6, max_length = 30, widget = forms.PasswordInput)
    password_again = forms.CharField(max_length = 30, widget = forms.PasswordInput)

    def clean_username(self):
        if (len(self.cleaned_data['username']) == 0):
            raise forms.ValidationError('Please enter a non-empty username')
        else:
            username = self.cleaned_data['username']
            if User.objects.filter(username = self.cleaned_data['username']):
                raise forms.ValidationError('This username is already taken. Please choose another.')
            else:
                return self.cleaned_data['username']

    def clean_password(self):
        if self.prefix:
            field_name1 = '%s-password'%self.prefix
            field_name2 = '%s-password_again'%self.prefix
        else:
            field_name1 = 'password'
            field_name2 = 'password_again'
            
        if self.data[field_name1] != '' and self.data[field_name1] != self.data[field_name2]:
            raise forms.ValidationError ("The entered passwords do not match.")
        else:
            return self.data[field_name1]

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
