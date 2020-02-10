from django.db import models

class memberShipPlan(models.Model):
    trainerName=models.CharField(max_length=60)
    classesName=models.CharField(max_length=60)
    price=models.IntegerField()
    time=models.IntegerField()
def __str__(self):
        return self.trainerName

