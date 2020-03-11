from django.db import models
from accounts.models import User
from countries.models import City

# Create your models here.

class Evaluation(models.Model):
    """Country Model"""
    opinion = models.TextField()
    user = models.ForeignKey(User, related_name='evaluations', on_delete=models.CASCADE, blank=True, default='')
    city = models.ForeignKey(City, related_name='evaluations', on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=50, blank=True, default='')
    classification = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opinion