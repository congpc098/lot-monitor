from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# view-functions take request -> response

def index(request):
    return render(request, 'monitor-lot.html', {})