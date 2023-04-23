from django.urls import path
from . import views


app_name = 'masters'

urlpatterns = [
    path("masters/", views.masters, name='masters'),
    # path('<int:discount_id>/', views.detail, name='detail'),
    # path('discount/<int:discount_id>/', views.detail, name='detail'),
]