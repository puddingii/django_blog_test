from django import forms
from .models import Account

#login form
class AccountLogin(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['acc_id', 'acc_password']

        widgets = {
            'acc_id':forms.TextInput(),
            'acc_password':forms.PasswordInput()
        }
        labels = {
            'acc_id': 'ID',
            'acc_password': 'Password'
        }

#singup form
class AccountSignup(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['acc_id', 'acc_password','password_chk']

        widgets = {
            'acc_id':forms.TextInput(),
            'acc_password':forms.PasswordInput(),
            'password_chk':forms.PasswordInput()
        }
        labels = {
            'acc_id': 'ID',
            'acc_password': 'Password',
            'password_chk': 'Password Check'
        }