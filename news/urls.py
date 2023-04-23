from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<int:news_id>/', views.detail, name='detail'),

]