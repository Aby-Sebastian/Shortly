from django.db import models
# from app.models import Tag
from django.utils import timezone
# Create your models here.

class AnonymousUsersLink(models.Model):
    url = models.CharField(max_length=100,unique=False)
    short_url = models.CharField(max_length=20,unique=True, blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True,blank=True)
    expiration_date = models.DateTimeField(blank=True)
    # tags = models.ManyToManyField(Tag, default='Anonymous', blank=True)

    # url_title = models.CharField(max_length=200,null=True,blank=True, default='No Title found')
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return str(self.short_url)

    def update(self, url):
        self.url = url
        return self.url

    def set_expiration_date(self):
    	self.expiration_date = self.date_created + timezone.timedelta(days=1)
    	return self.expiration_date