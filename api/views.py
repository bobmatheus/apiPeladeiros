from rest_framework import generics, permissions
from .models import CustomUser, Espaco, Reserva, ItemCarrinho
from .serializers import RegisterSerializer, EspacoSerializer, ReservaSerializer, ItemCarrinhoSerializer

# Registro de usuário
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    
# Listar espaços
class EspacoListView(generics.ListCreateAPIView):
    queryset = Espaco.objects.all()
    serializer_class = EspacoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Reservas
class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticated]

# Carrinho
class ItemCarrinhoListCreateView(generics.ListCreateAPIView):
    queryset = ItemCarrinho.objects.all()
    serializer_class = ItemCarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]