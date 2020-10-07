from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.username


class Order(models.Model):
    STATUS_CHOICES = [
        ('Reviewing', 'Reviewing'),
        ('Reviewed', 'Reviewed'),
        ('Charging', 'Charging'),
    ]
    user = models.ForeignKey(User,models.CASCADE)
    logo_url = models.URLField(blank=True)
    title = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    url = models.URLField()
    img_url = models.URLField(blank=True,default='default.png')
    category = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    size = models.CharField(max_length=300)
    Qty = models.IntegerField()
    statue = models.CharField(max_length=300,choices=STATUS_CHOICES)
    def __str__(self):
        return self.title

