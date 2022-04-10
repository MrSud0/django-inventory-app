from django.contrib import admin
from apps.miningapp.models import Hashrate,Motherboard,Coin, GPU
# Register your models here.
admin.site.register(Hashrate)
admin.site.register(Motherboard)
admin.site.register(Coin)


class GPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'wattage')
    list_filter = ("price",)
    search_fields = ['name']
    # prepopulated_fields = {'test': ('kappa',)}


admin.site.register(GPU, GPUAdmin)
