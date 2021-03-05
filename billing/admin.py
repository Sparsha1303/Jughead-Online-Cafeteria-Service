from django.contrib import admin
from .models import UdupiBillingProfile,TangoBillingProfile,MunchBillingProfile
# Register your models here.
admin.site.register(UdupiBillingProfile)
admin.site.register(TangoBillingProfile)
admin.site.register(MunchBillingProfile)