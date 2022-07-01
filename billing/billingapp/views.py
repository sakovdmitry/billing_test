from .models import Client, Organization, Bills
from rest_framework import viewsets, filters
from .serializers import (
    BillsSerializer,
    ClientSerializer,
    OrganizationSerializer
)
# from django.shortcuts import render
# import pandas as pd
# from rest_framework.response import Response
# from rest_framework import status


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


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('client_org', 'client_name') 
