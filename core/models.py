from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AbstractDate(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractUser(models.Model):
    created_by = models.ForeignKey(
        User, related_name='%(class)s_created_by',
        blank=True, on_delete=models.CASCADE)
    modified_by = models.ForeignKey(
        User, related_name='%(class)s_modified_by',
        null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
