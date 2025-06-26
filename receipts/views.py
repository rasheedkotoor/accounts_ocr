from rest_framework import viewsets, status, serializers
from .models import ReceiptFile, Receipt
from .serializers import (
    ReceiptFileSerializer,
    ReceiptFileUploadSerializer,
    ReceiptSerializer
)
from .ocr_pdf import extract_info_from_pdf


class ReceiptFileViewSet(viewsets.ModelViewSet):
    queryset = ReceiptFile.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReceiptFileUploadSerializer
        return ReceiptFileSerializer

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES.get('file')
        receipt_file = serializer.save(file_name=uploaded_file.name)

        # Validate PDF
        # try:
        print(f"receipt_file.file.path: {receipt_file.file.path}")
        data = extract_info_from_pdf(receipt_file.file.path)
        print(f"data: {data}")
        receipt_file.is_processed = True

        # except Exception as e:
        #     receipt_file.is_valid = False
        #     receipt_file.invalid_reason = str(e)
        #     receipt_file.is_processed = False

        receipt_file.save()
        return
