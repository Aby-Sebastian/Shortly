from django.core.management.base import BaseCommand,CommandError
from app.models import Links
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = "Expires event objects which are out-of-date"

    def handle(self, *args, **kwargs):
        # self.stdout.write("Working fine like a 100 year old wine :) ")
        # all_links = Links.objects.all()
        tz=timezone.get_default_timezone()
        try:
            all_links = Links.objects.filter(expiration_date__lt=datetime.datetime.now(tz=tz))
            for link in all_links:
                self.stdout.write(link.url)
                self.stdout.write(link.short_url)
            self.stdout.write(f"Total no of expiring links are {len(all_links)}")
            all_links.delete()
            self.stdout.write("All Expired links are deleted")
        except :
            self.stdout.write("Error occured")