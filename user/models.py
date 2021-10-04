from django.db import models
from core.models import AbstractDate
from django.contrib.auth.models import User
from organization.models import Organization
# Create your models here.

class UserProfile(User):
    int_phone = models.IntegerField(blank=True, null=True)
    char_address = models.CharField(
        max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'user_profile'
