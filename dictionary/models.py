from django.db import models
from django.utils import timezone


class Element(models.Model):
    code_element = models.CharField(max_length=50)
    value_element = models.CharField(max_length=250)

    def __str__(self):
        return self.value_element


class Version(models.Model):
    version = models.CharField(max_length=30)
    start_date = models.DateTimeField(default=timezone.now)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='version')

    def __str__(self):
        return self.version


class Catalog(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='catalog')

    def __str__(self):
        return self.name
