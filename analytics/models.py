from django.db import models
from django.contrib.auth.models import User
from app.models import Links

# Create your models here.

class Analytics(models.Model):
    '''
    Stores each click by date(single column for a day)
    '''
    url = models.ForeignKey(Links, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    click = models.PositiveIntegerField(null=True,blank=True,default=0)
    
    class Meta:
        ordering = ['-date']
        verbose_name = 'Analytics'
        verbose_name_plural = 'Analytics'

    def __str__(self):
        return self.url.url 

    def add_click(self):
        self.click+=1
        return self.click

    def update(self, *args, **kwargs):
        self.click +=1
        self.date = timezone.now()
        print('from analytics app models ',self.click)
        super().update(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.click +=1
        print('from analytics app models save overrided',self.click)
        super().save(*args, **kwargs)  

class Devices(models.Model):
    device_name = models.CharField(max_length=50)

    def __str__(self):
        return self.device_name

class Countries(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

class Ip_address(models.Model):
    date = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=50)

    def __str__(self):
            return f"{self.ip} on {self.date}"

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "IP address"

class Link_only_ip_address(models.Model):
    '''
    Stores each click by time (each day multiple columns)
    '''
    url = models.ForeignKey(Links, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=50)
    device = models.CharField(max_length=100, default='None')
    country = models.CharField(max_length=50, default='None')
    click = models.PositiveIntegerField(null=True,blank=True,default=0)
    # dev = models.ForeignKey(Devices, on_delete=models.CASCADE)
    # cou = models.ForeignKey(Countries, on_delete=models.CASCADE)
    # i_p = models.ForeignKey(Ip_address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ip} is in device {self.device} on {self.date.ctime()}"

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Link"