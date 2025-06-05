from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReceiptFileViewSet

router = DefaultRouter()
router.register(r'receipt-files', ReceiptFileViewSet, basename='receiptfile')

urlpatterns = [
    path('', include(router.urls)),
]
