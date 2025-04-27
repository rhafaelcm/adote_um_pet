from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animais/', views.listar_animais, name='listar_animais'),
    path('animais/<int:animal_id>/', views.detalhe_animal, name='detalhe_animal'),
    path('meus-animais/', views.meus_animais, name='meus_animais'),
    path('cadastrar-animal/', views.cadastrar_animal, name='cadastrar_animal'),
    path('editar-animal/<int:animal_id>/', views.editar_animal, name='editar_animal'),
    path('minhas-solicitacoes/', views.minhas_solicitacoes, name='minhas_solicitacoes'),
    path('solicitacoes-recebidas/', views.solicitacoes_recebidas, name='solicitacoes_recebidas'),
    path('responder-solicitacao/<int:solicitacao_id>/', views.responder_solicitacao, name='responder_solicitacao'),
]