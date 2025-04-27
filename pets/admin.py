from django.contrib import admin
from .models import Animal, Foto, SolicitacaoAdocao

class FotoInline(admin.TabularInline):
    model = Foto
    extra = 1

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'idade', 'cidade', 'estado', 'esta_adotado', 'data_cadastro']
    list_filter = ['tipo', 'idade', 'esta_adotado', 'cidade', 'estado']
    search_fields = ['nome', 'descricao', 'raca']
    inlines = [FotoInline]

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ['animal', 'eh_principal']
    list_filter = ['eh_principal']

@admin.register(SolicitacaoAdocao)
class SolicitacaoAdocaoAdmin(admin.ModelAdmin):
    list_display = ['animal', 'solicitante', 'status', 'data_solicitacao']
    list_filter = ['status', 'data_solicitacao']
    search_fields = ['animal__nome', 'solicitante__username', 'mensagem']
