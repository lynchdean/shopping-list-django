from django.db import models


class List(models.Model):
    name = models.CharField(max_length=60)
    items = models.CharField(max_length=200)
