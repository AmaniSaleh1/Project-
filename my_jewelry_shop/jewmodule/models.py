from django.db import models

class Jewelry(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    edition = models.IntegerField()

    def __str__(self):
        return self.title
