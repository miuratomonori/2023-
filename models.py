from django.db import models

# Create your models here.
class Day(models.Model):
    year = models.CharField('年月日',max_length=255)
    average = models.FloatField('平均気温')
    max = models.FloatField('最高気温')
    min = models.FloatField('最低気温')

class month(models.Model):
    year = models.IntegerField('年')
    average = models.FloatField('平均気温')