from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'remove expired otp codes'

    def handle(self, *args, **options):
        OtpCode.objects.filter(created__lt=datetime.now() - timedelta(minutes=5)).delete()
        self.stdout.write(self.style.SUCCESS('Successfully removed expired otp codes'))
