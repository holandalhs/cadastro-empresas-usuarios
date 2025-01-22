from django.shortcuts import render, redirect  
#from django.http import HttpResponse
#from .forms import FuncionarioForm  
#from .models import Empresa  
import pandas as pd  
from django.contrib.auth.models import User 
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def cadastrar_empresa(request):  
    #return HttpResponse('Testando')
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Acesso inválido!')
            return redirect('/empresas/cadastrar_empresa')
        
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Empresa já cadastrada!')
            return redirect('/empresas/cadastrar_empresa')
        

        try:
            user = User.objects.create_user(
                username=username,
                password=senha,
            )
            return redirect('/empresas/logar_empresa')
        except:
            messages.add_message(request, constants.ERROR, 'Erro do servidor!')
            return redirect('/empresas/cadastrar_empresa')


def logar_empresa(request):
    if request.method == 'GET':
        return render(request, 'logar_empresa.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
                                    ##colunaBanco=variável acima
    user = auth.authenticate(request, username=username, password=senha)
    if user:
        auth.login(request, user)
        messages.add_message(request, constants.SUCCESS, 'Logado!')
        return redirect('/funcionarios/cadastrar_funcionario/')
    else:
        messages.add_message(
            request, constants.ERROR, 'Username ou senha inválidos'
        )
        return redirect('/empresas/logar_empresa')


def logout(request):
    auth.logout(request)
    return redirect('/empresas/logar_empresa')



def exportar_empresas(request):  
    empresas = Empresa.objects.all().values()  
    df = pd.DataFrame(empresas)  

    # Salvando em um arquivo Excel  
    df.to_excel('empresas.xlsx', index=False)  

    return redirect('cadastrar_empresa')