# contato/api/views.py
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import (
    MensagemContato, Espaco, RegraPreco, Periodo,
    PrecoPeriodo, Feriado, Bloqueio, BloqueioRecorrente, Reserva
)
from .serializers import (
    MensagemContatoSerializer, EspacoSerializer, RegraPrecoSerializer,
    PeriodoSerializer, PrecoPeriodoSerializer, FeriadoSerializer,
    BloqueioSerializer, BloqueioRecorrenteSerializer, ReservaSerializer
)

class MensagemContatoViewSet(viewsets.ModelViewSet):
    queryset = MensagemContato.objects.all()
    serializer_class = MensagemContatoSerializer
    permission_classes = [AllowAny]

class EspacoViewSet(viewsets.ModelViewSet):
    queryset = Espaco.objects.all()
    serializer_class = EspacoSerializer
    permission_classes = [AllowAny]

class RegraPrecoViewSet(viewsets.ModelViewSet):
    queryset = RegraPreco.objects.all()
    serializer_class = RegraPrecoSerializer
    permission_classes = [AllowAny]

class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
    permission_classes = [AllowAny]

class PrecoPeriodoViewSet(viewsets.ModelViewSet):
    queryset = PrecoPeriodo.objects.all()
    serializer_class = PrecoPeriodoSerializer
    permission_classes = [AllowAny]

class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer
    permission_classes = [AllowAny]

class BloqueioViewSet(viewsets.ModelViewSet):
    queryset = Bloqueio.objects.all()
    serializer_class = BloqueioSerializer
    permission_classes = [AllowAny]

class BloqueioRecorrenteViewSet(viewsets.ModelViewSet):
    queryset = BloqueioRecorrente.objects.all()
    serializer_class = BloqueioRecorrenteSerializer
    permission_classes = [AllowAny]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [AllowAny]
