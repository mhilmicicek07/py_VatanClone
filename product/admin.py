from django.contrib import admin
from .models import *

# Register your models here.
class UrunAdmin(admin.ModelAdmin):
    list_display = ('id','urun_name','urun_description','urun_price')


admin.site.register(Kategori)
admin.site.register(Urun, UrunAdmin)