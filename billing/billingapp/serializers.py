from .models import Client, Organization, Bills
from rest_framework import serializers
import random


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
    fraud_score = serializers.SerializerMethodField()
    service_class = serializers.SerializerMethodField()
    service_name = serializers.SerializerMethodField()

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

    def get_fraud_score(self, service):
        return random.randit(0, 1)

    # def classificator(service):
    #     keys = [1, 2, 3, 4, 5]
    #     service_class = random.choice(keys)
    #     return service_class

    def get_service_class(self, service):
        keys = [1, 2, 3, 4, 5]
        service_class = random.choice(keys)
        return service_class

    def get_service_name(self, service_class):
        dictionary = {
            1: 'консультация',
            2: 'лечение',
            3: 'стационар',
            4: 'диагностика',
            5: 'лаборатория'
            }
        return dictionary[service_class]
