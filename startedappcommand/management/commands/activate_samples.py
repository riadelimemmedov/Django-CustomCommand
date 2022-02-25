from django.core.management.base import BaseCommand
from startedappcommand.models import *

class Command(BaseCommand):
    help = 'activate all unactivate samples'
    
    def handle(self, *args, **kwargs):
        size = Sample.objects.filter(activated=False).count()
        if (size != 0):
            qs = Sample.objects.filter(activated=False)
            count = 0
            for obj in qs:
                count += 1
                obj.activated = True
                obj.save()#f you have made a change, you must remember these changes in the language
            print(f"activated {count} data in database activated")
        else:
            print('nothing chance run command in database')