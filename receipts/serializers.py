from rest_framework import serializers
from .models import ReceiptFile, Receipt


class ReceiptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receipt
        fields = [
            'id', 'receipt_file', 'purchased_at',
            'merchant_name', 'total_amount', 'file_path',
            'created_at', 'updated_at'
        ]


class ReceiptFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptFile
        fields = ['file']


class ReceiptFileSerializer(serializers.ModelSerializer):
    receipts = ReceiptSerializer(many=True, read_only=True)

    class Meta:
        model = ReceiptFile
        fields = [
            'id', 'file', 'file_name', 'is_valid',
            'invalid_reason', 'is_processed', 'created_at',
            'updated_at', 'receipts'
        ]
