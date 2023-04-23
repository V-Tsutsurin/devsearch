from django.urls import path
from . import views


app_name = 'additional'

urlpatterns = [
    path('photos/', views.photos, name='photos'),
    # path('news/<int:news_id>/', views.detail, name='detail'),
    path('contacts/', views.contacts, name='contacts'),
]