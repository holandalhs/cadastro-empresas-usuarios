from django.urls import path  ##cadastrar as urls
from . import views
#from .views import cadastrar_funcionario, exportar_funcionarios  

urlpatterns = [
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('exportar_funcionarios/', views.exportar_funcionarios, name='exportar_funcionarios'), 
    ## a URL exportar_funcionarios que aponta para a função exportar_funcionarios
]


