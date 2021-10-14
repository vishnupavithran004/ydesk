from django.db import models
from core.models import AbstractDate, AbstractUser

# Create your models here.
class Organization(AbstractDate, AbstractUser):
    code = models.CharField(
        max_length=200, blank=True, null=True)
    name = models.CharField(
        max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'organization'
        

class Account(AbstractDate, AbstractUser):
    code = models.CharField(
        max_length=200, blank=True, null=True)
    name = models.CharField(
        max_length=200, blank=True, null=True)
    organization = models.ForeignKey(
        Organization, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'