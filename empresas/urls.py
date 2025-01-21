from django.urls import path  ##cadastrar as urls
from . import views
##from .views import cadastrar_empresa, exportar_empresas, logar_empresa, logout

urlpatterns = [
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),
    path('logar_empresa/', views.logar_empresa, name='logar_empresa'),
    path('logout/', views.logout, name='logout'),
    path('exportar_empresas/', views.exportar_empresas, name='exportar_empresas'), 

]

