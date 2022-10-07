from django.shortcuts import render
from django.http import HttpResponseRedirect
from gallery.models import Gallery
from .forms import GalleryForm

# Create your views here.

def gallery(request):
	data = Gallery.objects.all()
	
	if request.method == 'POST':
		form = GalleryForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('gallery')
	else:
		form = GalleryForm()
	return render(request, 'dashboard/gallery.html', {'form': form, 'data': data})

