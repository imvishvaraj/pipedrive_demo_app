from django.db import models

class Pipedrive(models.Model):
    key = models.CharField(max_length=20)

    def __str__(self):
        return self.key
