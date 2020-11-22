from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stock(models.Model):
    name = models.CharField(max_length=75)
    ticker= models.CharField(max_length=10, unique=True)
    popularity = models.IntegerField(default=0)
    def __str__(self):
        return "%s" % self.ticker

class Trader (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Stock)
    def __str__(self):
        return "%s" % self.user
class Comment(models.Model):
    text = models.CharField(max_length=1000)
    posted_on = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.ForeignKey(Stock, on_delete=models.CASCADE)
    def __str__(self):
        return "%s on %s" % (self.posted_by, self.about)
