from rest_framework import serializers
from myapp.models import *

class Usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def create(self, validated_data):
        user = Usuario(
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            email=validated_data['email'],
            age=validated_data['age'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user