from django.db import models

# Create your models here.


class PainPrediction(models.Model):
    seat_h = models.IntegerField()
    seat_d = models.IntegerField()
    seat_w = models.IntegerField()
    backrest_h = models.IntegerField()
    backrest_w = models.IntegerField()
    backrest_l = models.IntegerField()
    arm_h = models.IntegerField()
    arm_l = models.IntegerField()
    arm_distance = models.IntegerField()
    age = models.IntegerField()
