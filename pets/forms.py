from django import forms
from .models import Animal, Foto, SolicitacaoAdocao

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class AnimalForm(forms.ModelForm):
    fotos = MultipleFileField(required=False)
    
    class Meta:
        model = Animal
        fields = ['nome', 'tipo', 'raca', 'idade', 'sexo', 'descricao', 'cidade', 'estado']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
        }

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['imagem', 'eh_principal']

class SolicitacaoAdocaoForm(forms.ModelForm):
    class Meta:
        model = SolicitacaoAdocao
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Descreva por que você gostaria de adotar este animal e como pretende cuidar dele...'}),
        }