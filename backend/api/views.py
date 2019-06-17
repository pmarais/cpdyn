from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

class AccountsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

class UserAccountsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

    def retrieve(self, request, pk=None):
        queryset = Account.objects.all()
        accounts = queryset.filter(acc_client__pk=pk)
        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)

class TransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer

    def create(self, request):
        if request.data['tr_id'] == '':
            transaction, created = Transaction.objects.get_or_create(
                    tr_id = Transaction.objects.last().tr_id + 1,
                    tr_amount = float(request.data['tr_amount']),
                    tr_date = request.data['tr_date'],
                    tr_account = Account.objects.get(acc_id=request.data['tr_account'])
                )
        else:
            transaction, created = Transaction.objects.get_or_create(
                    tr_id = int(request.data['tr_id']),
                    tr_amount = float(request.data['tr_amount']),
                    tr_date = request.data['tr_date'],
                    tr_account = Account.objects.get(acc_id=request.data['tr_account'])
                )
        serializer = TransactionsSerializer(transaction)
        return Response(serializer.data)
        # return Response(None)

class AuthViewSet(viewsets.ViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

    def list(self, request):
        return Response(None)

    def create(self, request):
        clients = Client.objects.filter(cl_name__icontains=str(request.data['user']).lower())
        # print("Authing >>>>", request.data)
        if clients.count() > 0:
            client = clients[0]
            serializer = ClientsSerializer(client)
            print("Authing >>>>", serializer.data)
            if client.cl_pwd == int(request.data['pin']):
                return Response({'auth': True, 'client': serializer.data})
            else:
                return Response({'auth': False, 'client': None})
        else:
            return Response({'auth': False, 'client': None})

