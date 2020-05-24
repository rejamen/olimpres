from django.contrib import admin
from .models import SaleOrder

# Register your models here.
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ('code', 'partner_id', 'product_id')

admin.site.register(SaleOrder, SaleOrderAdmin)
