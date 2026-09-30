from django.db import models

class CropField(models.Model):
    name = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    soiltype = models.CharField(max_length=200)
    sowingmonth = models.CharField(max_length=200)
    harvestingmonth = models.CharField(max_length=200)
    fertilizer = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)

class MarketPrice(models.Model):
    cropname = models.CharField(max_length=200)
    marketname = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.DateField()

class ExpertForm(models.Model):
    name = models.CharField(max_length=200)
    phoneno = models.IntegerField()
    village = models.CharField(max_length=200)
    taluka = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    problem = models.CharField(max_length=200)

class Government(models.Model):
    name = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    link = models.CharField(max_length=200)

class FarmerTraining(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=200)
    contact = models.CharField(max_length=200)
    taluka = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    cropdetails = models.CharField(max_length=200)

class Newsupdate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posteddate = models.DateField()






# Create your models here.
