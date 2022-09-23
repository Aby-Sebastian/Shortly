from django.forms import TextInput, EmailInput, PasswordInput, CharField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    password1 = CharField(label="Password",widget=PasswordInput(attrs={'class':'form-control', 'id':'floatingPassword', 'placeholder':'Password', 'style':'margin-bottom: 0px; border-bottom-right-radius: 0; border-bottom-left-radius: 0;'}),
                                    help_text="<small><ul><li>Your password can't be too similar to your other personal information.</li>\
                                    <li>Your password must contain at least 8 characters.</li>\
                                    <li>Your password can't be a commonly used password.</li>\
                                    <li>Your password can't be entirely numeric.</li></ul></small>")
    password2 = CharField(label="Password confirmation", widget=PasswordInput(attrs={'class': 'form-control', 'id':'floatingPassword2', 'placeholder':'Passoword'}),\
                                help_text="<small>Enter the same password as before, for verification.</small>")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs={'class':"form-control" ,'id':"floatingInput", 'name':"username", 'placeholder':"Username"}),
            'email' : EmailInput(attrs={'class':"form-control", 'id':"floatingInputEmail", 'name':"email", 'placeholder':"name@example.com"}),
                    }
