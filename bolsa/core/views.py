from django.shortcuts import render
from core.models import Project

# Create your views here.
def portfolio(request):

   projects= Project.objects.all()
   return render(request, "core/portfolio.html", {'projects':projects})