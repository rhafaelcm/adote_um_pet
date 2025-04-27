"""
URL configuration for adote_um_pet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from pets.views_auth import logout_view

# Redirect para a página inicial
def accounts_redirect(request):
    return redirect('home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pets.urls')),
    # Adicionar redirecionamento para accounts/
    path('accounts/', accounts_redirect),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='pets/login.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name='pets/password_change.html', success_url='/accounts/password_change/done/'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='pets/password_change_done.html'), name='password_change_done'),
]

# Configuração para servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
