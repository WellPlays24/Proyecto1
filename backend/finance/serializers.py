from rest_framework import serializers
from .models import Profile, Transaction, Category

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'patrimonio_inicial', 'dinero_actual']  # Los campos que queremos exponer en la API

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'type', 'description', 'date', 'category']  # Los campos de Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']  # Los campos de Category


