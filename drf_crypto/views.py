from rest_framework.viewsets import ModelViewSet

from drf_crypto.models import Network, Transaction, Wallet
from drf_crypto.serializers import (
    NetworkSerializer,
    TransactionSerializer,
    WalletSerializer,
)


class NetworkViewSet(ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
