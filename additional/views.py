from django.shortcuts import render, get_object_or_404
from .models import Photos


def photos(request):
    photo_list = Photos.objects.order_by('-date')
    return render(request, 'additional/photos.html', {'photo_list': photo_list})


def contacts(request):
    return render(request, 'additional/contacts.html')
