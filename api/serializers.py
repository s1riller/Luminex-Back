from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import User, SkinType
from djoser.serializers import UserCreateSerializer

class CustomUserSerializer(UserSerializer):
    birth_date = serializers.DateField()

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ('birth_date',)

class SkinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinType
        fields = '__all__'