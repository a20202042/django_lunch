from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import mysite.models as models
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class store_form(forms.ModelForm):
    class Meta:
        model = models.Store
        fields = ["store_name", "store_number", "store_remake"]
    def __init__(self, *args, **kwargs):
        super(store_form, self).__init__(*args, **kwargs)
        self.fields['store_name'].label = "商店名稱"
        self.fields['store_number'].label = "0.0"
        self.fields['store_remake'].label = ".-."