from rest_framework import serializers
from testapp.models import Register
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields ='__all__'
