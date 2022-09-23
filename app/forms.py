from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField
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

    def save(self, commit=True):
        m = super(CreateCustomLinkForm, self).save(commit=False)
        # do custom stuff
        if commit:
            m.save()
        return m

