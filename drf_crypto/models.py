from uuid import uuid4

from django.db.models import (
    RESTRICT,
    DateTimeField,
    DecimalField,
    ForeignKey,
    Model,
    TextField,
    UUIDField,
)
from drf_shop.models import Currency

from drf_crypto.settings import AMOUNT_DECIMAL_PLACES, AMOUNT_MAX_DIGITS

# region Abstract Models


class BaseAbstractModel(Model):
    id: UUIDField = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        db_index=True,
    )
    created_at: DateTimeField = DateTimeField(
        auto_now_add=True,
        db_index=True,
    )
    modified_at: DateTimeField = DateTimeField(
        auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


# endregion

# region Core Models


class Network(BaseAbstractModel):
    name: TextField = TextField()
    currency: ForeignKey = ForeignKey(
        to=Currency,
        on_delete=RESTRICT,
        related_name="networks",
        db_index=True,
    )

    def __str__(self) -> str:
        return str(self.name)


class Wallet(BaseAbstractModel):
    private_key: TextField = TextField()
    address: TextField = TextField()

    def __str__(self) -> str:
        return str(self.address)


class Transaction(BaseAbstractModel):
    sender: TextField = TextField()
    receiver: TextField = TextField()
    amount: DecimalField = DecimalField(
        max_digits=AMOUNT_MAX_DIGITS,
        decimal_places=AMOUNT_DECIMAL_PLACES,
    )
    transaction_hash: TextField = TextField()

    def __str__(self) -> str:
        return str(self.transaction_hash)


# endregion
