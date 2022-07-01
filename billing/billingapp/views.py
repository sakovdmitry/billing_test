from .models import Client, Organization, Bills
from rest_framework import viewsets
from .serializers import (
    BillsSerializer,
    ClientSerializer,
    OrganizationSerializer
)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
