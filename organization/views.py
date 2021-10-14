from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Organization, Account
from .serializers import OrgSerializer, AccountSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating 
    deleting and editing organization instances 
    """
    serializer_class = OrgSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating 
    editing and deleting Account instances 
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]


