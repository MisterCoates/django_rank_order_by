from django.db import models


# Create your models here.
class RankTest(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    rating = models.DecimalField(max_digits=8, decimal_places=5)
