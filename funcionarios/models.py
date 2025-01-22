from django.db import models

# Create your models here.
class Categoria(models.Model):
    senioridade = models.CharField(max_length=20)
    def __str__(self):
        return self.nome



class Funcionario(models.Model):  
    nome = models.CharField(max_length=100)  
    cargo = models.CharField(max_length=100)  
    salario = models.DecimalField(max_digits=10, decimal_places=2)  
    data_admissao = models.DateField()  
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    ##chave estrangeira empresa vinculada ao funcionário

    def __str__(self):  
        return self.nome