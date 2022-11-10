from django.db import models

# Create your models here.


class Odam(models.Model):
    ism = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    yosh = models.IntegerField(default=12)