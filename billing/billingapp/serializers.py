from .models import Client, Organization, Bills
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'client_name', 'name', 'address')


class BillsSerializer(serializers.ModelSerializer):
    # вычислить 3 последних поля
    class Meta:
        model = Bills
        fields = (
            'id',
            'client_name',
            'client_org',
            'number',
            'sum',
            'date',
            'fraud_score',
            'service_class',
            'service_name'
            )
