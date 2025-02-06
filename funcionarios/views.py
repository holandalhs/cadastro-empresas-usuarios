from django.shortcuts import render, redirect  
#from django.http import HttpResponse
#from .forms import FuncionarioForm   
import pandas as pd  
from .models import Categoria, Funcionario
from django.contrib.messages import constants
from django.contrib import messages

def cadastrar_funcionario(request):  
    #return HttpResponse('Olá mundo')
    if not request.user.is_authenticated:
        return redirect('/empresas/logar_empresa/')
    
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        ##print(categoria) printar no terminal, teste
        return render(request, 'cadastrar_funcionario.html', {'categorias': categorias})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        salario = request.POST.get('salario')
        data_admissao = request.POST.get('data_admissao')
        senioridade = request.POST.get('senioridade')
        carta_apresentacao = request.POST.get('carta_apresentacao')

        """ if len(nome.strip()) == 0 or len(cargo.strip()) == 0:
            messages.add_message(request, constants.ERROR,
                                  "Obrigatório preencher os campos de nome e cargo.",)
            return redirect('/funcionarios/cadastrar_funcionario') """
        
        funcionario = Funcionario(
            user=request.user, ##a empresa para este funcionário, é a empresa logada 
            nome=nome,
            cargo=cargo,
            salario=salario,
            data_admissao=data_admissao,
            senioridade_id=senioridade, #por ser chave estrangeira passo _id
            carta_apresentacao=carta_apresentacao
        )
        funcionario.save()

        messages.add_message(request, constants.SUCCESS, "Funcionário cadastrado com sucesso.")
        return redirect('/funcionarios/cadastrar_funcionario')

  

   

def exportar_funcionarios(request):  
    funcionarios = Funcionario.objects.all().values()  
    df = pd.DataFrame(funcionarios)  

    # Salvando em um arquivo Excel  
    df.to_excel('funcionarios.xlsx', index=False)  
    messages.add_message(request, constants.SUCCESS, "Exportação realizada com sucesso.")

    return redirect('/funcionarios/cadastrar_funcionario')