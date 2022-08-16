from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

 

class Links(models.Model):
    url = models.CharField(max_length=100,unique=False)
    short_url = models.CharField(max_length=20,unique=True, blank=True, null=True)
    url_title = models.CharField(max_length=200,null=True,blank=True, default='No Title found')
    date_created = models.DateTimeField(auto_now_add=True,blank=True, editable=False)
    expiration_date = models.DateTimeField(blank=True)
    total_clicks = models.IntegerField(default=0, blank=True, null=True)
    tags = TaggableManager(blank=True)
    # taggs = models.ManyToManyField(Tag, default='test')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # qr_code = models.ImageField(upload_to='QR_codes',default='../static/images/young-man-avatar.jpg')

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return str(self.short_url)

    def increment_count(self):
        self.total_clicks+=1
        return self.total_clicks

    def update(self, url):
        self.url = url
        return self.url

    def save_qrcode(self):
        qrcode_img = qrcode.make(url_shortened + self.short_url)
        canvas = Image.new('RGB', (qrcode_img.pixel_size,qrcode_img.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        qrname = f"qr_code-{self.short_url}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(qrname, File(buffer), save=False)
        canvas.close()
        return self.qr_code


    class Meta:
        verbose_name_plural = "Link"






class Customer(models.Model):
    """docstring for Customer"""
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Customer"

