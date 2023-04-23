from django.urls import path
from . import views


app_name = 'discount'

urlpatterns = [
    path("", views.index, name='index'),
    # path('<int:discount_id>/', views.detail, name='detail'),
    path('discount/<int:discount_id>/', views.detail, name='detail'),
]