from django.db import models


class List(models.Model):
    name = models.CharField(max_length=60)
    items = models.JSONField(default=list)
