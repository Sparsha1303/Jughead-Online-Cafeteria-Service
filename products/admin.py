from django.contrib import admin
from .models import Tango,Udupi,Munch
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Tango
admin.site.register(Tango, ProductAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Udupi
admin.site.register(Udupi, ProductAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Munch
admin.site.register(Munch, ProductAdmin)