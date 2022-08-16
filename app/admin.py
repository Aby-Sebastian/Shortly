from django.contrib import admin
from .models import Links, Customer

# Register your models here.
# admin.site.register(Customer)
# admin.site.register(Tag)
class LinksAdmin(admin.ModelAdmin):
    list_display = [ 'url', 'short_url', 'date_created', 'expiration_date', 'total_clicks']
    list_per_page = 10
admin.site.register(Links,LinksAdmin)
