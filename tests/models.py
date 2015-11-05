from django.contrib.postgres.fields import ArrayField
from django.db import models


class TestModel(models.Model):
    ints = ArrayField(models.IntegerField(), null=True)
    strings = ArrayField(models.TextField(), null=True)
