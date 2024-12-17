from django.contrib import admin
from .models import Suppliers


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):

    list_display = ('supplier_name', 'supplier_bio')
    search_fields = ['supplier_name']
