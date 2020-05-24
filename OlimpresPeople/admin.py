from django.contrib import admin
from .models import Partner, City


class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email',
        'mobile', 'phone',
        'city_id'
    )


admin.site.register(Partner, PartnerAdmin)
admin.site.register(City)

