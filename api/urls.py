from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import (
    MensagemContatoViewSet, EspacoViewSet, RegraPrecoViewSet, PeriodoViewSet,
    PrecoPeriodoViewSet, FeriadoViewSet, BloqueioViewSet, BloqueioRecorrenteViewSet,
    ReservaViewSet
)

router = DefaultRouter()
router.register(r'mensagens', MensagemContatoViewSet)
router.register(r'espacos', EspacoViewSet)
router.register(r'regras-preco', RegraPrecoViewSet)
router.register(r'periodos', PeriodoViewSet)
router.register(r'precos-periodo', PrecoPeriodoViewSet)
router.register(r'feriados', FeriadoViewSet)
router.register(r'bloqueios', BloqueioViewSet)
router.register(r'bloqueios-recorrentes', BloqueioRecorrenteViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('auth/token/', obtain_auth_token),  # ⬅ endpoint de login com username/senha
    path('', include(router.urls)),
]