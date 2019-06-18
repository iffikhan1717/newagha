from django.db import models
from datetime import datetime


class Schemes(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    area = models.IntegerField()
    l_dt = models.DateTimeField(datetime.now)
    price  = models.DecimalField(max_digits=15, decimal_places=2)
    descp  = models.TextField()
    photo_m  = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_1  = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_2  = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    # price and total flats

    def __str__(self):
        return str(self.name)


class Flats(models.Model):
    sch = models.ForeignKey(Schemes,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=15)
    area   = models.IntegerField()
    price  = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    bedrms   = models.IntegerField()
    bthrms   = models.IntegerField()
    photo_m  = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1  = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)
    photo_2  = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True)


    def __str__(self):
        return str(self.f_name)
