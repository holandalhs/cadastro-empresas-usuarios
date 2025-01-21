from django.shortcuts import render, redirect  
#from django.http import HttpResponse
#from .forms import FuncionarioForm  
from .models import Funcionario  
import pandas as pd  

def cadastrar_funcionario(request):  
    #return HttpResponse('Olá mundo')
    """ if request.method == 'POST':  
        form = FuncionarioForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('cadastrar_funcionario')  
    else:  
        form = FuncionarioForm()  
    
    funcionarios = Funcionario.objects.all()  """ 

    return render(request, 'cadastrar_funcionario.html')
   

def exportar_funcionarios(request):  
    funcionarios = Funcionario.objects.all().values()  
    df = pd.DataFrame(funcionarios)  

    # Salvando em um arquivo Excel  
    df.to_excel('funcionarios.xlsx', index=False)  

    return redirect('cadastrar_funcionario')