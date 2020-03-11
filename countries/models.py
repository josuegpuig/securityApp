from django.db import models

# Create your models here.

class Country(models.Model):
    """Country Model"""
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = "Countries"

class State(models.Model):
    """State Model"""
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=200, blank=True, default='')
    code = models.CharField(max_length=10, blank=True, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    """City Model"""
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=200, blank=True, default='')
    code = models.CharField(max_length=10, blank=True, default='')
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name