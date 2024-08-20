from django.contrib import admin
from .models import Tours
# Register your models here.

class AdministrarTours(admin.ModelAdmin):
    list_display=('id','nombre','estado')
    search_fields=('nombre','estado','ciudad')
    date_hierarchy ='created'
    list_filter =('created','estado')

admin.site.register(Tours, AdministrarTours)