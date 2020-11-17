from django.shortcuts import render
from gallery.models import gallarey

def display(request):
    resultsdisplay=gallarey.objects.all()
    return render(request, 'index.html', {'gallarey': resultsdisplay})
    
