from django.db import models
from django.contrib.auth.models import User

class Animal(models.Model):
    TIPO_CHOICES = [
        ('cao', 'Cão'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('outro', 'Outro'),
    ]
    
    IDADE_CHOICES = [
        ('filhote', 'Filhote'),
        ('jovem', 'Jovem'),
        ('adulto', 'Adulto'),
        ('idoso', 'Idoso'),
    ]
    
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    raca = models.CharField(max_length=50, blank=True, null=True)
    idade = models.CharField(max_length=10, choices=IDADE_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    descricao = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    esta_adotado = models.BooleanField(default=False)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animais')
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return self.nome

class Foto(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='pets/')
    eh_principal = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Foto de {self.animal.nome}"

class SolicitacaoAdocao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('recusada', 'Recusada'),
    ]
    
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='solicitacoes')
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    mensagem = models.TextField()
    
    def __str__(self):
        return f"Solicitação de {self.solicitante.username} para {self.animal.nome}"
