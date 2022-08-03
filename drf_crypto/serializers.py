from rest_framework.fields import DateTimeField
from rest_framework.serializers import ModelSerializer

from drf_crypto.models import Network, Transaction, Wallet


class BaseSerializer(ModelSerializer):
    created_at: DateTimeField = DateTimeField(read_only=True)
    modified_at: DateTimeField = DateTimeField(read_only=True)

    class Meta:
        fields = [
            "id",
            "created_at",
            "modified_at",
        ]


class NetworkSerializer(BaseSerializer):
    class Meta:
        model = Network
        fields = [
            *BaseSerializer.Meta.fields,
            "name",
            "currency",
        ]


class WalletSerializer(BaseSerializer):
    class Meta:
        model = Wallet
        fields = [
            *BaseSerializer.Meta.fields,
            "private_key",
            "address",
        ]


class TransactionSerializer(BaseSerializer):
    class Meta:
        model = Transaction
        fields = [
            *BaseSerializer.Meta.fields,
            "sender",
            "receiver",
            "amount",
            "transaction_hash",
        ]
