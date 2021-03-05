from django.contrib import admin
from .models import UdupiOrder,TangoOrder,MunchOrder
# Register your models here.
admin.site.register(UdupiOrder)
admin.site.register(TangoOrder)
admin.site.register(MunchOrder)