from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrManager

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(business=self.request.user.business)

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            business=self.request.user.business,
            status='pending'
        )

    @action(detail=True, methods=['post'], permission_classes=[IsOwnerOrManager])
    def approve(self, request, pk=None):
        product = self.get_object()
        product.status = 'approved'
        product.save()
        return Response({'status': 'Product approved'})