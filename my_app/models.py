from django.db import models


class example(models.Model):
    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
    name = models.CharField(max_length=200)
    family = models.CharField(max_length=200)
    god = models.BooleanField()
