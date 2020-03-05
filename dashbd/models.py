from django.db import models
from jsonfield import JSONField
import json

class PDKey(models.Model):
    key = models.CharField(max_length=20)

    def __str__(self):
        return self.key

class Persons(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Deals(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name