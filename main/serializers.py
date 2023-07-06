from rest_framework import serializers
from main.models import Marks, Event, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'id', 'name', 'surname'
        ]


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
        instance.type = validated_data.get("type", instance.type)
        instance.save()

        return instance


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
