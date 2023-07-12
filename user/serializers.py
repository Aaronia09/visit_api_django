
from rest_framework import serializers
from user.models import user
from django.contrib.auth import authenticate

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

'''
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            email=data.get('email'),
            password=data.get('password')
        )
        if not user:
            raise serializers.ValidationError("Nom d'utilisateur ou mot de passe invalide.")
        data['user'] = user
        return data

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = user.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user
'''