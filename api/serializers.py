from rest_framework import serializers
from .models import CustomUser, Espaco, Reserva, ItemCarrinho
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)  # confirmação da senha

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "As senhas não conferem."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class EspacoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Espaco
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        if Reserva.objects.filter(espaco=data['espaco'], data=data['data']).exists():
            raise serializers.ValidationError("Espaço já reservado para esta data.")
        return data

class ItemCarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCarrinho
        fields = '__all__'