from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from .pagination import CustomPageNumberPagination


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = CustomPageNumberPagination

    
