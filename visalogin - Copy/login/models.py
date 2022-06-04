from django.db import models

# Create your models here.
class emplogin(models.Model):
    name=models.CharField(max_length=40)
    passportid=models.CharField(max_length=40)
    mofano=models.CharField(max_length=40)
    visano=models.IntegerField()
    visastatus=models.CharField(max_length=100)
    authorised=models.CharField(max_length=100)

    class Meta:
        db_table='emplogin'
