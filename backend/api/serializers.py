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
    acc_balance = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = '__all__'

    def get_acc_balance(self, obj):
        return obj.get_balance()['balance']

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        # read_only_fields = ('tr_id', )

class ClientsGetSerializer(serializers.ModelSerializer):
    # cl_accounts = AccountsSerializer(read_only=True)
    class Meta:
        model = Client
        fields = '__all__'