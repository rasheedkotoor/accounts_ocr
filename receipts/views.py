from rest_framework import viewsets, status, serializers
from .models import ReceiptFile, Receipt
from .serializers import (
    ReceiptFileSerializer,
    ReceiptFileUploadSerializer,
    ReceiptSerializer
)


class ReceiptFileViewSet(viewsets.ModelViewSet):
    queryset = ReceiptFile.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReceiptFileUploadSerializer
        return ReceiptFileSerializer

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES.get('file')
        receipt_file = serializer.save(file_name=uploaded_file.name)

        # TODO validate the pdf file
        # Validate if ends with .pdf
        if receipt_file.file_name.lower().endswith('.pdf'):
            receipt_file.is_valid = True
            receipt_file.invalid_reason = ""
        else:
            raise serializers.ValidationError("Only PDF files are allowed.")

        # TODO Process PDF using OCR if valid
        receipt_file.save()
        return
