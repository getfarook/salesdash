from django.contrib import admin
from . import models
# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['area','type']



admin.site.register(models.Area)
admin.site.register(models.Partner, PartnerAdmin)
admin.site.register(models.ProductCat)
admin.site.register(models.Product)
