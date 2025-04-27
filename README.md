# Adote um Pet 🐱🐶

Este é um projeto de extensão universitária da Anhanguera, criado por Rhafael da Costa Martins cursando Sistemas de Informação. A plataforma conecta animais que precisam de um lar com pessoas dispostas a adotá-los.

## Sobre o Projeto

Adote um Pet é uma vitrine digital para animais disponíveis para adoção. Nossos principais recursos incluem:

- Galeria de animais para adoção com fotos e informações detalhadas
- Sistema de busca e filtragem por tipo de animal, idade e localização
- Perfis detalhados de cada animal com características e necessidades específicas
- Sistema de contato direto entre adotantes e responsáveis pelos animais
- Área de login para responsáveis cadastrarem e gerenciarem seus animais

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Banco de dados**: PostgreSQL (configurável para usar SQLite durante desenvolvimento)
- **Armazenamento das fotos**: Sistema de arquivos local

## Configuração do Ambiente

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- PostgreSQL (opcional - pode usar SQLite para desenvolvimento)

### Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/adote-um-pet.git
   cd adote-um-pet
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   - Para usar SQLite (padrão para desenvolvimento), não é necessária configuração adicional.
   - Para usar PostgreSQL, descomente a configuração correspondente no arquivo `adote_um_pet/settings.py` e ajuste as credenciais.

5. Execute as migrações:
   ```
   python manage.py migrate
   ```

6. Crie um superusuário (administrador):
   ```
   python manage.py createsuperuser
   ```

7. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```

8. Acesse o sistema em `http://127.0.0.1:8000/`

## Estrutura do Projeto

- `adote_um_pet/` - Configurações principais do Django
- `pets/` - Aplicativo principal com modelos, views e templates
- `templates/` - Templates HTML compartilhados
- `static/` - Arquivos estáticos (CSS, JS, imagens)
- `media/` - Arquivos enviados pelos usuários (fotos dos pets)

## Funcionalidades

### Para Visitantes
- Visualizar animais disponíveis para adoção
- Filtrar animais por tipo, idade e localização
- Ver detalhes de cada animal

### Para Usuários Logados
- Cadastrar animais para adoção
- Gerenciar seus animais (editar informações, marcar como adotado)
- Solicitar a adoção de animais
- Responder a solicitações de adoção
- Acompanhar o status das solicitações enviadas

## Contribuindo

Se você deseja contribuir com este projeto, por favor:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Autor

**Rhafael da Costa Martins** - Estudante de Sistemas de Informação - Anhanguera

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.