import re
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,get_list_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.utils import timezone
import uuid
import qrcode
import qrcode.image.svg
from io import BytesIO
from .forms import CreateLinkForm, CreateCustomLinkForm
from files.forms import UploadFileForm
from .models import Links, Customer
from files.models import Files
from analytics.models import Analytics
from taggit.models import Tag # taggit model
from anonymous_data.models import AnonymousUsersLink
from django.utils.text import slugify
from django.db.models import Q, F
from django.db.models import Sum
from django.views.generic import TemplateView
# Create your views here.

def home(request):
	'''
		index page
	'''
	sform = CreateLinkForm()
	
	if request.method == 'POST':
		form = CreateLinkForm(request.POST)
		if form.is_valid():
			value=form['url'].value()
			uid = str(uuid.uuid4())[:5]
			if request.user.is_anonymous:
				# user = get_object_or_404(User, username="AnonymousUser")
				expiration = timezone.now() + timezone.timedelta(minutes=5)
				new = AnonymousUsersLink(url=value,short_url=uid,expiration_date=expiration)
				new.save()
			return render(request,'main/index.html',{'form':sform,'url':value,'short_url':uid})
	else:
		sform = CreateLinkForm()
	return render(request,'main/index.html',{'form':sform})

def anonymous_save(request):
	''' saves anonymous users web urls '''
	if request.method == 'POST':
		form = CreateLinkForm(request.POST)
		if form.is_valid():
			value=request.POST.get('inp_url')
			uid = str(uuid.uuid4())[:5]
			
			# user = get_object_or_404(User, username="AnonymousUser")
			expiration = timezone.now() + timezone.timedelta(minutes=5)
			new = AnonymousUsersLink(url=value,short_url=uid,expiration_date=expiration)
			new.save()
			return JsonResponse({'status':1,'short_url':uid})
		return JsonResponse({'status':0})

def link_shortner(request,pk):
	url=Links.objects.filter(short_url=pk)[0]
	return render(request,'main/index.html',{'url':url,'short_url':pk})


def get_client_ip(request):
	''' gets ip address '''
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip

# def get_country_from_IP(ip_address):
# 	reader = geoip2.database.Reader('./GeoLite2-Country/GeoLite2-Country.mmdb')
# 	try:
# 		response = reader.country(ip_address)
# 		country_name = response.country.name

# 	except geoip2.errors.AddressNotFoundError:
# 		print("Its localhost you idiot")
# 		country_name = 'India'

# 	reader.close()
# 	return country_name

from files.models import Files

def fileShare(request,pk):
	''' File redirecting '''
	file = get_object_or_404(Files, share_url=pk)
	return redirect(file.document.url)

def go(request,pk):
	''' website resharing '''
	# try:
	#     url_details=Links.objects.get(short_url=pk)
	# except :
	#     print('DoesNotExist')
	if request.user.is_anonymous:
		obj = get_object_or_404(AnonymousUsersLink, short_url=pk)
	else:
		obj = get_object_or_404(Links, short_url=pk)
		day = Analytics.objects.filter(url=obj,date__date=timezone.now().date()) # Check if someone checked this url today
		
		if day:
			"""
			if someone checked url this day update click by one
			"""
			click = Analytics.objects.filter(url=obj,date__date=timezone.now().date()).update(click=F('click')+1,date=timezone.now())
			
			obj.increment_count()
			obj.save()
			
		else:
			"""
			if no one checked this url this day create new instance for this date
			"""
			click = Analytics(url=obj) 
			click.save()	
			click.url.increment_count()		# Increments url click count by 1
			click.url.save(update_fields=['total_clicks'])				# saves b.url class


	# ua = request.headers.get('User-Agent')
	# # print(ua)
	# # Parse UA string and load data to dict of 'os', 'client', 'device' keys
	# device = DeviceDetector(ua).parse()
	# link_ip = get_client_ip(request)
	# country = get_country_from_IP(link_ip)
	# # print(country)
	# page = Customer.objects.get(short_url=pk)

	

	# print(page.count)

	# saving user ip and details to models
	# b = Link_only_ip_address(ip=link_ip, url=page, country=country, device=device.os_name(), click=page.total_clicks+1)
	# b.url.increment_count()		# Increments url click count by 1
	# b.url.save()				# saves b.url class
	# b.save()					# saves b
	
	return redirect(obj.url)


# Parsing title from url
from urllib.request import urlopen, Request
from lxml.html import parse

def title_parser(url):
	''' 
		Extracts sites title metadata from url 
		dependencies : lxml, urllib
	'''
	# url = "https://www.google.com"

	# To-Do : place this code in a try for exception handling.
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req)
	p = parse(page)
	result = p.find(".//title").text
	print(result)
	return result

def user_ceated_links(request):
	''' 
		user creted links 
	'''
	if request.user.is_anonymous:
		
		user_specific = Links.objects.filter(user=2)
	else:
		user_specific = Links.objects.filter(user=request.user.id)
	form = CreateCustomLinkForm()
	if request.method == 'POST':
		form = CreateCustomLinkForm(request.POST)
		
		if form.is_valid():
			lid = request.POST.get('sid')
			value=form['url'].value()
			short_url = form['short_url'].value()
			expiration = timezone.now() + timezone.timedelta(days=30)
			try:
				url_title = title_parser(value)
			except:
				url_title = 'No Page Found'
			
			if lid == '':
				custom_url = Links(url=value,short_url=short_url,expiration_date=expiration,user=request.user)
			else:
				custom_url = Links(id=lid,url=value,short_url=short_url,expiration_date=expiration,user=request.user)
			custom_url.save()
	else:
		
		form = CreateCustomLinkForm()

	context = {'user_links':user_specific, 'form':form}
	return render(request,'user/user_links.html',context=context)

def reset_short_url(request):
	pass

@login_required(login_url='login')
def showall(request):
	data = Links.objects.all().order_by('-date_created')
	return render(request, 'main/show_links.html',{'data':data})

def showallusers(request):
	users = User.objects.filter(is_staff=False)
	return render(request,'user/show_users.html', {'data':users})

def delete(request):
	
	if request.method == 'POST':
		id = request.POST.get('sid')
		url=Links.objects.get(pk=id)
		url.delete()
		return JsonResponse({'status':1, 'id':id})
	return JsonResponse({'status':0})

def edit_links(request):
	if request.method == 'POST':
		id = request.POST.get('sid')
		link = Links.objects.get(pk=id)
		tags = [tag.name for tag in link.tags.all()]
		
		link_data = {'id':link.id, 'url':link.url, 'short_url':link.short_url, 'tags': tags}
		return JsonResponse(link_data)
	return JsonResponse({'status':0})

from django.core import serializers

def edit(request):
	'''
		edit method returns in json form
	'''
	if request.method == 'POST':
		
		id = request.POST.get('id')
		url = request.POST.get('url')
		short_url = request.POST.get('short_url')

		link = Links.objects.get(pk=id)
		sid = Links.objects.get(pk=id)
		form = CreateCustomLinkForm(request.POST, instance=sid)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user = request.user
			
			obj.short_url = short_url
			
			obj.save()
			# Without this next line the tags won't be saved.
			form.save_m2m()
			
			
			

		
		
			response_tags = [tag.name for tag in link.tags.all()]
			resp = {'id':link.id, 'url':link.url, 'short_url':link.short_url, 'tags':response_tags, 'messages':'Link edited successfully.'}
		
			messages.success(request, 'Link edited successfully.')
			return JsonResponse(resp)
	messages.error(request, form.errors)
	return JsonResponse({'status':0})

from django.core import serializers

def dashboard(request):
	chart = Analytics.objects.filter().values('date__date').order_by('-date__date').annotate(sum=Sum('click'))
	l_user = Links.objects.filter(user=request.user).order_by('-total_clicks')
	l_all = Links.objects.aggregate(Sum('total_clicks'))['total_clicks__sum']
	context = { 'l_all': l_all, 'l_user': l_user, 'top_3': l_user[:3], 'chart':chart}
	return render(request, 'dashboard/dashboard.html', context=context)

def dashboard_chart_api(request):
	chart = Analytics.objects.filter().values('date__date').order_by('-date__date').annotate(sum=Sum('click'))[:7]
	chart_label = [date['date__date'] for date in chart ]
	chart_clicks = [sum['sum'] for sum in chart]
	
	return JsonResponse({'chart_label':chart_label, 'chart_clicks':chart_clicks})

def settingsPage(request):
	user = User.objects.get(pk=request.user.id)
	return render(request, 'dashboard/settings.html', {'user':user})

def tagsPage(request):
	# tags = Tag.objects.all()
	z=Links.objects.filter(user=request.user.id)
	s=z.values('tags').distinct() # gets distinct tags from users links
	tags=Tag.objects.filter(id__in=s)
	return render(request, 'dashboard/tags.html', {'tags':tags})

from shorty.settings import WEB_ADDRESS

print(WEB_ADDRESS)

# def generate_qrcode(short_url):
# 	qrcode_img = qrcode.make(WEB_ADDRESS + self.short_url)
# 	canvas = Image.new('RGB', (qrcode_img.pixel_size,qrcode_img.pixel_size), 'white')
# 	draw = ImageDraw.Draw(canvas)
# 	canvas.paste(qrcode_img)
# 	qrname = f"qr_code-{self.short_url}.png"
# 	buffer = BytesIO()
# 	canvas.save(buffer, 'PNG')
# 	self.qr_code.save(qrname, File(buffer), save=False)
# 	canvas.close()
# 	return self.qr_code

def filesPage(request):
	user_specific = Files.objects.filter(user=request.user.id).order_by('-uploaded_at')
	
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			# file is saved
			obj = form.save(commit=False)
			obj.user = request.user
			obj.share_url = str(uuid.uuid4())[:5]
			obj.save()
			messages.success(request, 'File uploaded successfully.')
			# return HttpResponseRedirect('/success/url/')
	else: 
		form = UploadFileForm()
	return render(request, 'dashboard/files.html', {'form': form, 'data': user_specific})

def deleteFile(request):
	
	if request.method == 'POST':
		id = request.POST.get('sid')
		file=Files.objects.get(pk=id)
		file.document.delete()
		file.delete()
		return JsonResponse({'status':1, 'id':id})
	return JsonResponse({'status':0})

def temp(request):
	return render(request, 'dashboard/temp.html')

def log(request):
	return render(request, 'user/login.html')

def reg(request):
	return render(request, 'user/register.html')

def save_data(request):
	if request.method == 'POST':

		lid = request.POST.get('sid')
		
		if lid == '':
			
			form = CreateCustomLinkForm(request.POST)
		else:
			
			linkid = Links.objects.get(pk=lid)
			form = CreateCustomLinkForm(request.POST, instance=linkid)
		
		uid = str(uuid.uuid4())[:5]
		
		if form.is_valid():
			value=request.POST['url']
			short_url = request.POST['short_url']
			if short_url == '':
				short_url = uid
			
			expiration = timezone.now() + timezone.timedelta(days=30)
			try:
				title_url=title_parser(value)
			except:
				title_url = "No Page Found"
			
			if lid == '':
				custom_url = Links(url=value,short_url=short_url, url_title=title_url, expiration_date=expiration,user=request.user)
				custom_url.save()
			else:
				inst = Links.objects.filter(pk=lid) # Instance

				inst.update(url=value,short_url=short_url,expiration_date=expiration, url_title=title_url)

			
			messages.success(request, 'Link created successfully.')
			return JsonResponse({'status': 'save'})
		else:
			messages.error(request, form.errors)
			return JsonResponse({'status': 0})



def qr_code(request, short_url):
	'''Creates QR code each time this function is called '''
	context = {}
	if request.method == "POST":
		factory = qrcode.image.svg.SvgImage
		img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
		stream = BytesIO()
		img.save(stream) 
		context["svg"] = stream.getvalue().decode()
	return render(request, "qrModal.html", context=context)


def test_links(request):
	''' Links page section '''
	user_specific = Links.objects.filter(user=request.user.id).order_by('-date_created')

	paginator = Paginator(user_specific, 10,orphans=1)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	sform = CreateCustomLinkForm()
	
	if request.method == 'POST':
		form = CreateCustomLinkForm(request.POST)
		
		url=request.POST.get('url')

		short_url = request.POST.get('short_url')
		if short_url == '':
				uid = str(uuid.uuid4())[:5]
				short_url = uid

		
		if form.is_valid():
			
			url=request.POST.get('url')
			short_url = request.POST.get('short_url')
			
			if short_url == '':
				uid = str(uuid.uuid4())[:5]
				short_url = uid
			
			expiration = timezone.now() + timezone.timedelta(days=30)
			try:
				title_url=title_parser(url)
			except:
				title_url = "No Page Found"
			
			custom_url = Links(url=url,short_url=slugify(short_url), url_title=title_url, expiration_date=expiration,user=request.user)
			obj = form.save(commit=False)
			obj.user = request.user
			obj.expiration_date = expiration
			obj.short_url = short_url
			obj.url_title = title_url
			obj.save()
			# Without this next line the tags won't be saved.
			form.save_m2m()
			# custom_url.save()
			# custom_url.tags.save()
			messages.success(request, 'Link created successfully.')

		else:
			messages.error(request, form.errors)

	context = {'data': page_obj, 'form':sform}
	return render(request, 'dashboard/links.html', context)

def search(request):
	''' Returns search results from Links model that contains query '''
	query = request.GET.get('q')
	object_list = Links.objects.filter(
		Q(url__icontains=query) | Q(short_url__icontains=query) | Q(url_title__icontains=query)
		)
	return render(request, 'dashboard/search_results.html',{'object_list':object_list})



def post_list(request, tag_slug=None):
	
	# post tag
	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		z=Links.objects.filter(user=request.user.id)
		posts = z.filter(tags__in=[tag])	
	
	return render(request,'dashboard/post_list.html',{'posts':posts, 'tag':tag})

def ind(request):
	return render(request, 'main/indexa.html')
	
# page link layout
def page_link(request):

	return render(request,'dashboard/link_page.html')
# Clear up code to understand it better

def analytics_data(request):
	return render(request, 'components/analytics.html')

def mnb(i):
	return i.date.date(), i.click

def dashboard_or_analytics_chart(request):
	
	Analytics.objects.filter(date__date__gte=timezone.now().date()-timezone.timedelta(6), date__date__lte=timezone.now().date())
	Analytics.objects.filter(date__date__gte=timezone.now().date()-timezone.timedelta(6), date__date__lte=timezone.now().date(),url=10).aggregate(Sum('click'))['click__sum']
	'''will get and count clicks of last 7 days'''
	Analytics.objects.aggregate(Sum('click')) # total clicks happened using shortened urls
	'''will return links raging from gte date to lte date'''
	return JsonResponse({"hi":'hii'}) 

def analytics(request):
	'''
		Analytics data for links page for chart
	'''
	obj = request.GET.get('url')
	link = Links.objects.get(id=obj)
	s = Analytics.objects.filter(url=link)
	x=list(map(mnb,s))
	labels = []
	data = []
	for i in range(len(x)):
		labels.append(x[i][0])
		data.append(x[i][1])

	return JsonResponse({'status': x, 'id': obj, 'labels': labels, 'data': data})

def PagenotFound(request, exception):
	return render(request, "main/404.html")

def ServernotFound(request):
	return render(request, "main/500.html")