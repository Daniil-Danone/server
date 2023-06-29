from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import Todo
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["email", "name", "surname"]

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
