from django.db import models
from core.models import AbstractDate, AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class Category(AbstractDate, AbstractUser):
    code = models.CharField(
        max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'category'
    

class Topic(AbstractDate, AbstractUser):
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'topic'


class Questions(AbstractDate, AbstractUser):
    question = models.TextField(blank=True, null=True)
    header = models.CharField(
        max_length=50, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    answered_by = models.ForeignKey(
        User, models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey(
        Topic, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        db_table = 'questions'
    
