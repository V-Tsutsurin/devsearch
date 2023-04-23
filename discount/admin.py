from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class DiscountAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Discount
        fields = '__all__'


class DiscountAdmin(admin.ModelAdmin):
    form = DiscountAdminForm


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Slider)
