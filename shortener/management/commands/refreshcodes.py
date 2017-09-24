from django.core.management.base import BaseCommand, CommandError
from shortener.models import MyBitlyUrl


class Command(BaseCommand):
    help = 'Refreshes all MyBitlyUrl shortcodes'
    
    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **kwargs):
        return MyBitlyUrl.objects.refresh_shortcodes(items=['items'])
