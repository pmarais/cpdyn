from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class ClientsGetSerializer(serializers.ModelSerializer):
    cl_accounts = AccountsSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'