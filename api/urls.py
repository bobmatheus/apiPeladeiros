from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, EspacoListView, ReservaListCreateView, ItemCarrinhoListCreateView

urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('espacos/', EspacoListView.as_view(), name='espaco-list'),
    path('reservas/', ReservaListCreateView.as_view(), name='reserva-list'),
    path('carrinho/', ItemCarrinhoListCreateView.as_view(), name='carrinho-list'),
]