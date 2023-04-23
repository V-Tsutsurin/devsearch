from django.contrib import admin
from .models import Servicec
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ServicecAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Servicec
        fields = '__all__'
        verbose_name = 'Введите текст новости'


class ServicecAdmin(admin.ModelAdmin):
    form = ServicecAdminForm

admin.site.register(Servicec, ServicecAdmin)

