from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import BaseRouter

from drf_crypto.settings import DEBUG
from drf_crypto.views import NetworkViewSet, TransactionViewSet, WalletViewSet

router: BaseRouter
if DEBUG:
    router = routers.DefaultRouter()
else:
    router = routers.SimpleRouter()

router.register(r"_networks", NetworkViewSet)
router.register(r"_wallets", WalletViewSet)
router.register(r"_transactions", TransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
