from typing import Any, Optional
from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
from pytz import timezone


class Command(BaseCommand):
    help = 'remove all expired otp codes'

    def handle(self, *args, **options):
        expired_time = datetime.now(tz=timezone(
            'Asia/Teran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write('all expired otp codes removed')
