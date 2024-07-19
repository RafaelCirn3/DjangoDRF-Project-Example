from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.personagem.views import PersonagemViewSet
from apps.arma.views import ArmaViewSet
from apps.avatar.views import AvatarViewSet

# Configurando o roteador para as views
router = DefaultRouter()
# Registrando o ViewSet do modelo Personagem
router.register(r'personagens', PersonagemViewSet)
# Registrando o ViewSet do modelo Arma
router.register(r'armas', ArmaViewSet)
# Registrando o ViewSet do modelo Avatar
router.register(r'avatares', AvatarViewSet)

# Definindo as URLs do projeto
urlpatterns = [
    # URL para a interface de administração
    path('admin/', admin.site.urls),
    # URL para a API, incluindo as rotas configuradas pelo roteador
    path('api/', include(router.urls)),
]
