import datetime

def global_settings(request):
    """Adiciona variáveis globais para todos os templates."""
    return {
        'year': datetime.datetime.now().year,
    }