from django.urls import path
from . import views


app_name = 'services'

urlpatterns = [
    path("services/", views.services, name='services'),
    # path('<int:discount_id>/', views.detail, name='detail'),
    # path('discount/<int:discount_id>/', views.detail, name='detail'),
]