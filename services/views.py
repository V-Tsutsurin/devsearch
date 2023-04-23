from django.shortcuts import render, get_object_or_404
from .models import Servicec


def services(request):
    seviceslist1 = Servicec.objects.filter(work_type='1')
    seviceslist2 = Servicec.objects.filter(work_type='2')
    seviceslist3 = Servicec.objects.filter(work_type='3')
    sevices_list = {
        'sevices1': seviceslist1,
        'sevices2': seviceslist2,
        'sevices3': seviceslist3,
    }

    return render(request, 'services/services.html', sevices_list)
