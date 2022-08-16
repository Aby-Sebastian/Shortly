from django.contrib import admin
from .models import Analytics, Devices, Countries, Ip_address, Link_only_ip_address

# Register your models here.

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ['url','date','click',]
    

admin.site.register(Analytics, AnalyticsAdmin)
admin.site.register(Devices)
admin.site.register(Countries)
admin.site.register(Ip_address)
admin.site.register(Link_only_ip_address)