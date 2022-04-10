# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
# TODO currency model class-enum
# TODO currency brand class-enum

BRAND = (
    (0, "Unknown"),
    (1, "Gigabyte"),
    (2, "Asus")
)
MODEL = (
    (0, "No value"),
    (1, "1660super"),
    (2, "rx6800xt"),
    (3, "3070"),
    (4, "3070lhr"),
    (5, "3070ti")
)


class Locale(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    name = models.CharField(max_length=200, unique=False, null=True)
    description = models.CharField(max_length=200, unique=False, null=True)
    short_name = models.CharField(max_length=200, unique=False, null=True)


class Price(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    value = models.FloatField()
    shop = models.CharField(max_length=200, unique=False, null=True)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


class Wattage(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    value = models.CharField(max_length=200, unique=False)


class Overclock(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    memory_oveclock = models.CharField(max_length=200, unique=False)
    core_overclock = models.CharField(max_length=200, unique=False)
    core_voltage = models.CharField(max_length=200, unique=False)
    memory_controller_voltage = models.CharField(max_length=200, unique=False)
    memory_voltage = models.CharField(max_length=200, unique=False)
    power_limit = models.CharField(max_length=200, unique=False)
    soc_frequency = models.CharField(max_length=200, unique=False)
    soc_vddmax = models.CharField(max_length=200, unique=False)


class MiningRig(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=False)
    description = models.CharField(max_length=200, unique=False)


class RAM(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    capacity = models.CharField(max_length=200, unique=False)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)


class PSU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    wattage = models.CharField(max_length=200, unique=False)
    efficiency = models.CharField(max_length=200, unique=False)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)
    noise = models.CharField(max_length=200, unique=False)


# TODO Chip manufacturer to be enumeration
class CPU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    chip_manufacturer = models.CharField(max_length=200, unique=False)
    chipset = models.CharField(max_length=200, unique=False)
    core_clock = models.CharField(max_length=200, unique=False)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)


class Motherboard(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=False)
    brand = models.CharField(max_length=200, unique=False)
    pcie_slots = models.IntegerField()
    cpu_chip = models.CharField(max_length=200, unique=False)


class Fan(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=False)
    brand = models.CharField(max_length=200, unique=False)
    model = models.CharField(max_length=200, unique=False)
    rpm = models.CharField(max_length=200, unique=False)
    wattage = models.CharField(max_length=200, unique=False)
    noise = models.CharField(max_length=200, unique=False)
    width = models.CharField(max_length=200, unique=False)
    height = models.CharField(max_length=200, unique=False)
    length = models.CharField(max_length=200, unique=False)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)


class RigCase(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    brand = models.CharField(max_length=200, unique=False)
    model = models.CharField(max_length=200, unique=False)
    width = models.CharField(max_length=200, unique=False)
    height = models.CharField(max_length=200, unique=False)
    length = models.CharField(max_length=200, unique=False)
    open_air = models.BooleanField()
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)


# TODO  Price will be updated dynamically
# TODO Each GPU must have a msrp price
# https://github.com/AbenOG/skroutz_price_compare
class GPU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=False, null=True)
    brand = models.IntegerField(choices=BRAND, default=0)
    model = models.IntegerField(choices=MODEL, default=0)
    memory = models.CharField(max_length=200, unique=False, null=True)
    memory_manufacturer = models.CharField(max_length=200, unique=False, null=True)
    pcie_slots = models.IntegerField()
    wattage = models.ForeignKey(Wattage, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, unique=False, null=True, )
    overclock = models.ForeignKey(Overclock, on_delete=models.CASCADE)
    live_price = models.ForeignKey(Price, on_delete=models.CASCADE)
    price = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name




class Coin(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=200, unique=False)
    price = models.FloatField()
    currency = models.CharField(max_length=200, unique=False)
    live_price = models.ForeignKey(Price, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)


# Value is hash / second
class Hashrate(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    value = models.FloatField()




class OperationCenter(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)


class ProfitabilityExperiment(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)


class ProfitabilityForecast(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=True)
