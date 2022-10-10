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

			return HttpResponseRedirect('/gallery')
	else:
		form = GalleryForm()
	return render(request, 'dashboard/gallery.html', {'form': form, 'data': data})


def delete_img(request):
	if request.method == 'POST':
		key = request.POST.get('id')
		try:
			obj = Gallery.objects.get(id=key)
			obj.delete()
			print('done')
		except Exception as e:
			raise
	return HttpResponseRedirect('/gallery')