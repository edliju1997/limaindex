from django.shortcuts import render

from .models import Portfolio

def index(request):
    home = Portfolio.objects.all()
    template_name = 'core/index.html'
    context = {'index': home}
    return render(request, template_name, context)
