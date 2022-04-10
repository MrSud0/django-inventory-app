# -*- encoding: utf-8 -*-

from django.db import models


# Create your models here.
# TODO currency model class-enum
# TODO currency brand class-enum

BRAND = (
    (0,"Unknown"),
    (1,"Gigabyte"),
    (2,"Asus")
)
MODEL = (
    (0, "No value"),
    (1, "1660super"),
    (2, "rx6800xt"),
    (3, "3070"),
    (4, "3070lhr"),
    (5, "3070ti")
)



#TODO  Price will be updated dynamically
# https://github.com/AbenOG/skroutz_price_compare
class GPU(models.Model):
    name = models.CharField(max_length=200, unique=False, null=True )
    brand = models.IntegerField(choices=BRAND,default=0)
    model = models.IntegerField(choices=MODEL, default=0)
    memory = models.CharField(max_length=200, unique=False, null=True )
    memory_manifacturer = models.CharField(max_length=200, unique=False, null=True )
    wattage = models.CharField(max_length=200, unique=False)
    price = models.FloatField()
    comments = models.CharField(max_length=200, unique=False, null=True )

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name

# TODO currency class-enum
class Coin(models.Model):
    name = models.CharField(max_length=200, unique=False)
    price = models.FloatField()
    currency = models.CharField(max_length=200, unique=False)

# Value is hash / second
class Hashrate(models.Model):
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    value = models.FloatField()


# TODO brand class-enum
class Motherboard(models.Model):
    name = models.CharField(max_length=200, unique=False)
    brand = models.CharField(max_length=200, unique=False)
    pcie_slots = models.IntegerField()
    pcie_slots = models.IntegerField()
    cpu_chip = models.CharField(max_length=200, unique=False)
