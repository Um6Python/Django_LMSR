from django.core.management.base import BaseCommand
from market.models import LMSRMarket

class Command(BaseCommand):
    help = 'Initialize the LMSRMarket'

    def handle(self, *args, **kwargs):
        if not LMSRMarket.objects.exists():
            LMSRMarket.objects.create(name='Default Market', b=1.0, q={'outcome1': 0, 'outcome2': 0})
            self.stdout.write(self.style.SUCCESS('Successfully created the LMSRMarket'))
        else:
            self.stdout.write(self.style.SUCCESS('LMSRMarket already exists'))