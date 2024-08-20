"""
URL configuration for recorridos_mexico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from tours import views as views_tours
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.principal, name="principal"),
    path('catalogos/',views_tours.catalogos,name="catalogos"),
    path('nosotros/',views.nosotros, name="nosotros"),
    path('favoritos/',views.favoritos,name="favoritos"),
    path('login/', views.login, name='login'),
    path('cuenta/',views.cuenta,name="cuenta"),
    path('cerrar/',views.cerrar_sesion,name="cerrar_sesion"),
    path('registro/',views.registro,name="registro"),
    #path('registro/',views.sesion,name="registro"),
    path('tours/',views_tours.tours,name="tours"),
    path('mich/',views_tours.mich,name="mich"),
    path('qro/',views_tours.qro,name="qro"),
    path('realizados/',views_tours.realizados,name="realizados"),
    path('detalle_tour/<int:id>/',views_tours.detalle_tour,name="detalle_tour")
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 