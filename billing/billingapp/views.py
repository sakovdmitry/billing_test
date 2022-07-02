from .models import Organization, Bills
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .serializers import (
    BillsSerializer,
    ClientSerializer,
    OrganizationSerializer
)
import pandas as pd
from django.db.models import Count
# def simple_upload(request):
#     if request.method == 'POST':
#         excel_file = request.FILES
#         df = pd.read_excel(excel_file, sheet_name=0)
#         serializer = ClientSerializer(data=df)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         df = pd.read_excel(excel_file, sheet_name=1)
#         serializer = OrganizationSerializer(data=df)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
#     return render(request, 'index.html')


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer

    def create(self, request, *args, **kwargs):
        excel_file = request.FILES
        df = pd.read_excel(excel_file, sheet_name=0)
        serializer1 = ClientSerializer(data=df)
        if serializer1.is_valid():
            serializer1.save()
        df = pd.read_excel(excel_file, sheet_name=1)
        serializer2 = OrganizationSerializer(data=df)
        if serializer2.is_valid():
            serializer2.save()
        serializers_list = [serializer1, serializer2]
        content = {
            'status': 1,
            'responseCode': status.HTTP_200_OK,
            'data': serializers_list
        }
        return(Response(content))

    def get_queryset(self):
        queryset = (
            Organization.objects
            .values('client_name')
            .annotate(org_count=Count('client_org'), sum_bills=Count('sum'))
        )
        return queryset


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('client_org', 'client_name')

    def create(self, request, *args, **kwargs):
        excel_file = request.FILES
        df = pd.read_excel(excel_file, sheet_name=0)
        serializer = BillsSerializer(data=df)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
