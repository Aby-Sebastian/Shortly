from django.contrib import admin
from anonymous_data.models import AnonymousUsersLink

# Register your models here.
class AnonymousUsersLinkAdmin(admin.ModelAdmin):
	list_display = ['url','short_url','date_created','expiration_date']

admin.site.register(AnonymousUsersLink, AnonymousUsersLinkAdmin)