from django.db import models

# Create your models here.
class Person(models.Model):
    personname=models.CharField(max_length=120)
    age=models.IntegerField()
    salary=models.IntegerField()
    desig=models.CharField(max_length=120)

    def __str__(self):
        return self.personname







