from .models import Files
from django.forms import ModelForm, FileField, FileInput

class UploadFileForm(ModelForm):
    document = FileField(widget=FileInput(attrs={"class":"form-control me-2"}))
    
    class Meta:
        model = Files
        fields = ('document', 'user', 'share_url')