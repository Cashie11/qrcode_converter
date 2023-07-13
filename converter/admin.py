from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import QRCode

class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('data', 'created_at', 'display_qr_code')
    list_filter = ('created_at',)
    search_fields = ('data',)

    def display_qr_code(self, obj):
        return mark_safe('<img src="{}" width="100" height="100" />'.format(obj.code.url))
    display_qr_code.short_description = 'QR Code'

admin.site.register(QRCode, QRCodeAdmin)



