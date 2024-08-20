from django.contrib import admin
from .models import Usuarios
# Register your models here.
class AdministrarUsuarios(admin.ModelAdmin):
    list_display=('nombre','estado')
    search_fields=('nombre','estado','ciudad')
    date_hierarchy ='created'
    list_filter =('created','estado')

admin.site.register(Usuarios, AdministrarUsuarios)