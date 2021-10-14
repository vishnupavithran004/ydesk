from rest_framework import serializers
from .models import Organization, Account


class OrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"