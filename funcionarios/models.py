from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    senioridade = models.CharField(max_length=20)
    #default='senioridade'
    def __str__(self):
        return self.senioridade



class Funcionario(models.Model):  
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ##chave estrangeira empresa vinculada ao funcionário
    nome = models.CharField(max_length=100)  
    cargo = models.CharField(max_length=100)  
    salario = models.DecimalField(max_digits=10, decimal_places=2)  
    data_admissao = models.DateField()  
    senioridade = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True, blank=True)
    carta_apresentacao = models.TextField(default='Sem carta de apresentação')

    def __str__(self):  
        return self.nome