from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from funcionarios.models import Funcionario, Categoria
import logging
logging.basicConfig(level=logging.DEBUG)

class FuncionarioViewTests(TestCase):
    def setUp(self):
        logging.debug("Iniciando setUp do TestCase")
        self.client = Client()
        # Cria um usuário de teste
        self.user = User.objects.create_user(username='teste', password='12345')
        # Cria uma categoria de teste, que será utilizada como chave estrangeira
        self.categoria = Categoria.objects.create(nome='Categoria Teste')

    def test_cadastrar_funcionario_sem_autenticacao(self):
        logging.debug("Acesso sem autenticação é redirecionado para página de login")
        response = self.client.get('/funcionarios/cadastrar_funcionario/')
        self.assertRedirects(response, '/empresas/logar_empresa/')

    def test_get_cadastrar_funcionario_autenticado(self):
        logging.debug("Efetua o login do usuário de teste")
        self.client.login(username='teste', password='12345')
        logging.debug("Acessa a view via GET e verifica o status, template e contexto")
        response = self.client.get('/funcionarios/cadastrar_funcionario/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastrar_funcionario.html')
        self.assertIn('categorias', response.context)

    def test_post_cadastrar_funcionario_autenticado(self):
        self.client.login(username='teste', password='12345')
        # Define os dados do formulário para criar um novo funcionário
        dados = {
            'nome': 'João da Silva',
            'cargo': 'Desenvolvedor',
            'salario': '5000',
            'data_admissao': '2023-02-01',
            'senioridade': self.categoria.id,  # Envia o ID da categoria
            'carta_apresentacao': 'Experiência sólida em Python e Django'
        }
        response = self.client.post('/funcionarios/cadastrar_funcionario', dados)
        logging.debug("Verifica o redirecionamento após o POST de cadastro de funcionários")
        self.assertRedirects(response, '/funcionarios/cadastrar_funcionario')
        logging.debug("Confirma se o funcionário foi criado no banco de dados")
        self.assertTrue(Funcionario.objects.filter(nome='João da Silva').exists())
        # Verifica se a mensagem de sucesso foi adicionada ao request
        messages_list = list(get_messages(response.wsgi_request))
        self.assertTrue(any("cadastrado com sucesso" in m.message for m in messages_list))

