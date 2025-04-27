from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Animal, Foto, SolicitacaoAdocao
from .forms import AnimalForm, FotoForm, SolicitacaoAdocaoForm

def home(request):
    animais_destaque = Animal.objects.filter(esta_adotado=False).order_by('-data_cadastro')[:6]
    return render(request, 'pets/home.html', {
        'animais_destaque': animais_destaque,
    })

def listar_animais(request):
    tipo = request.GET.get('tipo', '')
    idade = request.GET.get('idade', '')
    localizacao = request.GET.get('localizacao', '')
    
    animais = Animal.objects.filter(esta_adotado=False)
    
    if tipo:
        animais = animais.filter(tipo=tipo)
    if idade:
        animais = animais.filter(idade=idade)
    if localizacao:
        animais = animais.filter(Q(cidade__icontains=localizacao) | Q(estado__icontains=localizacao))
    
    return render(request, 'pets/listar_animais.html', {
        'animais': animais,
        'tipo': tipo,
        'idade': idade,
        'localizacao': localizacao,
    })

def detalhe_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    form_solicitacao = SolicitacaoAdocaoForm() if request.user.is_authenticated else None
    
    if request.method == 'POST' and request.user.is_authenticated:
        form_solicitacao = SolicitacaoAdocaoForm(request.POST)
        if form_solicitacao.is_valid():
            solicitacao = form_solicitacao.save(commit=False)
            solicitacao.animal = animal
            solicitacao.solicitante = request.user
            solicitacao.save()
            messages.success(request, 'Solicitação de adoção enviada com sucesso!')
            return redirect('detalhe_animal', animal_id=animal.id)
    
    return render(request, 'pets/detalhe_animal.html', {
        'animal': animal,
        'form_solicitacao': form_solicitacao,
    })

@login_required
def meus_animais(request):
    animais = Animal.objects.filter(responsavel=request.user)
    return render(request, 'pets/meus_animais.html', {
        'animais': animais,
    })

@login_required
def cadastrar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.responsavel = request.user
            animal.save()
            
            # Processar as fotos
            for foto in request.FILES.getlist('fotos'):
                Foto.objects.create(
                    animal=animal,
                    imagem=foto,
                    eh_principal=Foto.objects.filter(animal=animal).count() == 0  # Primeira foto é a principal
                )
            
            messages.success(request, 'Animal cadastrado com sucesso!')
            return redirect('meus_animais')
    else:
        form = AnimalForm()
    
    return render(request, 'pets/cadastrar_animal.html', {
        'form': form,
    })

@login_required
def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id, responsavel=request.user)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            
            # Processar novas fotos
            for foto in request.FILES.getlist('fotos'):
                Foto.objects.create(
                    animal=animal,
                    imagem=foto,
                )
            
            messages.success(request, 'Animal atualizado com sucesso!')
            return redirect('meus_animais')
    else:
        form = AnimalForm(instance=animal)
    
    return render(request, 'pets/editar_animal.html', {
        'form': form,
        'animal': animal,
    })

@login_required
def minhas_solicitacoes(request):
    solicitacoes = SolicitacaoAdocao.objects.filter(solicitante=request.user)
    return render(request, 'pets/minhas_solicitacoes.html', {
        'solicitacoes': solicitacoes,
    })

@login_required
def solicitacoes_recebidas(request):
    animais = Animal.objects.filter(responsavel=request.user)
    solicitacoes = SolicitacaoAdocao.objects.filter(animal__in=animais)
    
    return render(request, 'pets/solicitacoes_recebidas.html', {
        'solicitacoes': solicitacoes,
    })

@login_required
def responder_solicitacao(request, solicitacao_id):
    solicitacao = get_object_or_404(
        SolicitacaoAdocao, 
        pk=solicitacao_id, 
        animal__responsavel=request.user
    )
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['aprovada', 'recusada']:
            solicitacao.status = status
            solicitacao.save()
            
            if status == 'aprovada':
                # Marcar o animal como adotado
                solicitacao.animal.esta_adotado = True
                solicitacao.animal.save()
                
                # Recusar outras solicitações pendentes
                SolicitacaoAdocao.objects.filter(
                    animal=solicitacao.animal,
                    status='pendente'
                ).exclude(pk=solicitacao.pk).update(status='recusada')
                
            messages.success(request, f'Solicitação {status}!')
        
        return redirect('solicitacoes_recebidas')
    
    return render(request, 'pets/responder_solicitacao.html', {
        'solicitacao': solicitacao,
    })
