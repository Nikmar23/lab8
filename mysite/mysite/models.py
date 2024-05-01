from django.db import models

class Clients(models.Model):
    ClientID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=255)
    AccountNumber = models.CharField(max_length=255)
    Phone = models.CharField(max_length=15)
    ContactPerson = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)

class Cars(models.Model):
    CarID = models.AutoField(primary_key=True)
    CarBrand = models.CharField(max_length=255, choices=[('fiesta', 'Fiesta'), ('focus', 'Focus'), ('fusion', 'Fusion'), ('mondeo', 'Mondeo')])
    NewCarCost = models.FloatField()
    Client = models.ForeignKey(Clients, on_delete=models.CASCADE)

class Repair(models.Model):
    RepairID = models.AutoField(primary_key=True)
    StartDate = models.DateField()
    Car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    RepairType = models.CharField(max_length=255, choices=[('warranty', 'Warranty'), ('scheduled', 'Scheduled'), ('major', 'Major')])