from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'this command runnner code'
    
    def handle(self,*args, **kwargs):
        print('Worked this datarunner commands')