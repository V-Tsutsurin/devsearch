from django.shortcuts import render, get_object_or_404
from .models import Discount, Slider


def index(request):
    discount = Discount.objects.order_by('-date')
    slider = Slider.objects.all()
    context = {
        'discounts': discount,
        'sliders': slider
    }
    return render(request, 'discount/index.html', context)


def detail(request, discount_id):
    discount_obj = get_object_or_404(Discount, pk=discount_id)
    return render(request, 'discount/discount_page.html', {'discount': discount_obj})
