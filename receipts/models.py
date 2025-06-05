from django.db import models


class ReceiptFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.FilePathField(path="/path/to/your/upload/folder", max_length=500)
    is_valid = models.BooleanField(default=False)
    invalid_reason = models.TextField(blank=True, null=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name


class Receipt(models.Model):
    receipt_file = models.ForeignKey(ReceiptFile, on_delete=models.CASCADE, related_name='receipts')
    purchased_at = models.DateTimeField(blank=True, null=True)
    merchant_name = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    file_path = models.FileField(upload_to='receipts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.merchant_name or 'Unknown'} - {self.purchased_at or 'No Date'}"
