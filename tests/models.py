from django.contrib.postgres.fields import ArrayField
from django.db import models


class TestModel(models.Model):
    ints = ArrayField(models.IntegerField())
