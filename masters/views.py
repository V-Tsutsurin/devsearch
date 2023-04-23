from django.shortcuts import render, get_object_or_404
from .models import Master


def masters(request):
    master = Master.objects.order_by('name')
    master1 = Master.objects.filter(location='1')
    master2 = Master.objects.filter(location='2')
    masters_all = {
        'masters': master,
        'master1': master1,
        'master2': master2
    }
    return render(request, 'masters/masters.html', masters_all)
