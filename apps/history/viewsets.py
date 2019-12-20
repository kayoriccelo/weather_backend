from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import History
from .serializers import HistorySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('date', 'search')
