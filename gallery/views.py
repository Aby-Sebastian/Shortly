from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from gallery.models import Gallery
from .forms import GalleryForm

# Create your views here.

@login_required(login_url='login')
@cache_control(must_revalidate=True, max_age=300)
def gallery(request):
	data = Gallery.objects.filter(user=request.user.id)
	if request.method == 'POST':
		print('post')
		form = GalleryForm(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			obj.save()
			
			messages.success(request, 'Image uploaded successfully.')
			return HttpResponseRedirect('/gallery')
	else:
		form = GalleryForm()
	return render(request, 'dashboard/gallery.html', {'form': form, 'data': data})

@login_required(login_url='login')
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