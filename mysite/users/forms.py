from django import forms

# 導入User 這個內建model(User)和內建的form(UserCreationForm)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# 繼承內建的UserCreationForm，再自己增加客製化欄位
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
