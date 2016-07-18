from django.contrib import admin
from basic.models import Region,barcode

class barcodeAdmin(admin.ModelAdmin):
    fields=('description',)

# Register your models here.
admin.site.register(Region)
admin.site.register(barcode,barcodeAdmin)
