from django.db import models

class Jewelry(models.Model):
    title = models.CharField(max_length=60)
    type = models.CharField(max_length=60)  # Changed 'author' to 'type'
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title
