from rest_framework import serializers
from django.contrib.auth import get_user_model
from main.models import Marks, Event
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


class MarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = "__all__"

    def create(self, validated_data):
        return Marks.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.author = validated_data.get("author", instance.author)
        instance.xpos = validated_data.get("xpos", instance.xpos)
        instance.ypos = validated_data.get("ypos", instance.ypos)
        instance.save()

        return instance


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
