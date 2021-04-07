from rest_framework import viewsets, filters
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'created_at',)
    ordering = ('created_at',)
