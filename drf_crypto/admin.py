from django.contrib import admin

from drf_crypto.models import Network, Transaction, Wallet


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
