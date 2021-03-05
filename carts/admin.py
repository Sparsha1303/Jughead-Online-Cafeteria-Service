from django.contrib import admin

# Register your models here.
from .models import UdupiCart, TangoCart, MunchCart

admin.site.register(UdupiCart)
admin.site.register(TangoCart)
admin.site.register(MunchCart)