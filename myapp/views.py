from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = LimitOffsetPagination
