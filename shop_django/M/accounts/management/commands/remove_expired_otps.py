from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz


class Command(BaseCommand):
    help = 'remove expired otp codes'

    def handle(self, *args, **options):
        OtpCode.objects.filter(created__lt=datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)).delete()
        self.stdout.write(self.style.SUCCESS('Successfully removed expired otp codes'))
