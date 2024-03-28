from django.db import models

class jewelry(models.Model):
    title = models.CharField(max_length = 60)
    author = models.CharField(max_length = 60)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)