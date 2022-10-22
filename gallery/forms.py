from django import forms
from .models import Gallery

class GalleryForm(forms.ModelForm):
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
	alt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alt text for image'}))

	class Meta:
		model = Gallery
		fields = ('image', 'alt', 'user')