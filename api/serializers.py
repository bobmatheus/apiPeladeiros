from rest_framework import serializers
from .models import (
    MensagemContato, Espaco, RegraPreco, Periodo, PrecoPeriodo,
    Feriado, Bloqueio, BloqueioRecorrente, Reserva, Usuario
)

class MensagemContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensagemContato
        fields = '__all__'

class EspacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espaco
        fields = '__all__'

class RegraPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegraPreco
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class PrecoPeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecoPeriodo
        fields = '__all__'

class FeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feriado
        fields = '__all__'

class BloqueioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloqueio
        fields = '__all__'

class BloqueioRecorrenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloqueioRecorrente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# ---- Novo Serializer para Cadastro ----
class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'password', 
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)  # senha criptografada
        usuario.save()
        return usuario
