from django.test import TestCase

from models import NG 
# Create your tests here.

def query_NG():
    a = NG.objects.all()
    print(a)