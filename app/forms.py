from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagField
from .models import Links



class CreateLinkForm(ModelForm):
    url = CharField(empty_value=False,required=True, widget=TextInput(attrs={'class':'form-control me-2', 'name':'url', 'placeholder':"Shorten your link"}))

    class Meta:
        model = Links
        fields = ['url']
    # url = CharField(label="url", widget=TextInput(attrs={'class':"form-control me-2" ,'name':"url", 'placeholder':"Shorten your link"}))
    

class CreateCustomLinkForm(ModelForm):
    short_url = CharField(empty_value=True,required=False, widget=TextInput(attrs={'class':"form-control shorturl-inp", 'id':"short_url", 'name':"short_url", 'placeholder':"Custom short url"}))
    # tags = CharField(empty_value=True,required=False, widget=TextInput(attrs={'class':"form-control shorturl-inp", 'id':"tags", 'name':"tags", 'placeholder':"tags"}))
    
    class Meta:
        model = Links 
        fields = ['url','short_url','tags']
        widgets = {
            'url' : TextInput(attrs={'class':"form-control url-inp", 'id':"url", 'name':"url", 'placeholder':"Url"}),
            # 'short_url' : TextInput(attrs={'class':"form-control", 'id':"floatingInputEmail", 'name':"short_url", 'placeholder':"Custom short url"}),
            "tags": TextInput(attrs={'class':"form-control url-inp", "placeholder" : "Add tags here. ","data-role": "tagsinput"})
                    }
    # tags = TagField()

    def save(self, commit=True):
        m = super(CreateCustomLinkForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m


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
