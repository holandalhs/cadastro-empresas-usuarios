from django.urls import path  ##cadastrar as urls
from . import views
#from .views import cadastrar_funcionario, exportar_funcionarios  

urlpatterns = [
    path('cadastrar_funcionario/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('exportar_funcionarios/', views.exportar_funcionarios, name='exportar_funcionarios'), 
]


