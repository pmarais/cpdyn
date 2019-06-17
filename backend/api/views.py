from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from rest_framework.response import Response

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

class TransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer

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
            accounts = client.cl_accounts.all()
            # serializer = ClientsSerializer(client)
            serializer = ClientsGetSerializer(client)
            print("Authing >>>>", serializer.data)
            if client.cl_pwd == int(request.data['pin']):
                return Response({'auth': True, 'client': serializer.data})
            else:
                return Response({'auth': False, 'client': None})
        else:
            return Response({'auth': False, 'client': None})

