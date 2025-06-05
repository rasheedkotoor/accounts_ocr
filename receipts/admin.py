from django.contrib import admin
from .models import ReceiptFile, Receipt


@admin.register(ReceiptFile)
class ReceiptFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'is_valid', 'invalid_reason', 'is_processed', 'updated_at')
    list_filter = ('is_valid', 'is_processed', 'created_at')
    search_fields = ('file_name', 'invalid_reason')


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'merchant_name', 'purchased_at', 'total_amount', 'updated_at')
    list_filter = ('purchased_at', 'created_at')
    search_fields = ('merchant_name',)
