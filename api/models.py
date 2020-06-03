from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class Statistics(models.Model):
    week = models.CharField(max_length=100)
    data = models.FloatField(default=0)

    def to_json(self):
        return {
            'id': self.id,
            'week': self.week,
            'data': self.data
        }
class Service(models.Model):
    title = models.CharField(max_length=300)
    logo = models.CharField(max_length=1000)
    category = models.CharField(max_length=500)
    position = models.FloatField(default=0)
    isActive = models.BooleanField(default=False)



    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'rating': self.rating
        }


class MyManager(models.Manager):
    def for_user(self, user):
        return self.filter(username=user)