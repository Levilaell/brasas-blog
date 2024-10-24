from django.shortcuts import get_object_or_404, render

from ..models import Service


def index(request):

    services = Service.objects.all()

    context = {
        'services': services
    }

    return render(request, 'service/index.html', context)

def service_details(request, id):
    
    service = get_object_or_404(Service, id=id)

    context = {
        'service': service
    }

    return render(request, 'service/service-details.html', context)

def about(request):

    return render(request, 'service/about.html')

def calendar(request):

    return render(request, 'service/calendar.html')

def services(request):

    services = Service.objects.all()

    context = {
        'services': services
    }
    
    return render(request, 'service/services.html', context)

def vision(request):

    return render(request, 'service/vision.html')