from rest_framework import serializers
from apps.session.models import Session


class SessionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Session # this will take all fields
        fields= "__all__"