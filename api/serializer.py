from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class Usersserializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

