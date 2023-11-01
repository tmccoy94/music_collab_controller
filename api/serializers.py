from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        # id is the model primary key added in the background by Django framework
        fields = ("id", "code", "host", "guest_can_pause", "votes_to_skip", "created_at")