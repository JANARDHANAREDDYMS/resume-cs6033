from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def resume(request):
    template = loader.get_template('studentinfo.html')
    return HttpResponse(template.render())