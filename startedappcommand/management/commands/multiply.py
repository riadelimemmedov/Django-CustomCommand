from django.core.management.base import BaseCommand
from startedappcommand.models import *

class Command(BaseCommand):
    help = 'count sample multiplication'
    
    def add_arguments(self,parser):
        parser.add_argument('param', type=int)#example => param=5
        
    def handle(self,*args, **options):#run edende isleyecek funksiya
        param = options.get('param')#formdan deyer almaga benzeyir
        count = Sample.objects.all().count()
        multiply = param*count
        print('Multiply',multiply)
    