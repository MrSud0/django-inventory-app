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
    name = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    description = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    short_name = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'locale'


class Price(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    value = models.FloatField()
    shop = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE, blank=True, default=None, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'price'



class Wattage(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    value = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'wattage'



class Overclock(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    memory_oveclock = models.CharField(max_length=200, unique=False, blank=True, default=None)
    core_overclock = models.CharField(max_length=200, unique=False, blank=True, default=None)
    core_voltage = models.CharField(max_length=200, unique=False, blank=True, default=None)
    memory_controller_voltage = models.CharField(max_length=200, unique=False, blank=True, default=None)
    memory_voltage = models.CharField(max_length=200, unique=False, blank=True, default=None)
    power_limit = models.CharField(max_length=200, unique=False, blank=True, default=None)
    soc_frequency = models.CharField(max_length=200, unique=False, blank=True, default=None)
    soc_vddmax = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'overclock'



class MiningRig(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)
    description = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'miningrig'



class RAM(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    capacity = models.CharField(max_length=200, unique=False, blank=True, default=None)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'ram'



class PSU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    wattage = models.CharField(max_length=200, unique=False, blank=True, default=None)
    efficiency = models.CharField(max_length=200, unique=False, blank=True, default=None)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)
    noise = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'psu'



# TODO Chip manufacturer to be enumeration
class CPU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    chip_manufacturer = models.CharField(max_length=200, unique=False, blank=True, default=None)
    chipset = models.CharField(max_length=200, unique=False, blank=True, default=None)
    core_clock = models.CharField(max_length=200, unique=False, blank=True, default=None)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'cpu'



class Motherboard(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)
    brand = models.CharField(max_length=200, unique=False, blank=True, default=None)
    pcie_slots = models.IntegerField()
    cpu_chip = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'motherboard'



class Fan(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)
    brand = models.CharField(max_length=200, unique=False, blank=True, default=None)
    model = models.CharField(max_length=200, unique=False, blank=True, default=None)
    rpm = models.CharField(max_length=200, unique=False, blank=True, default=None)
    wattage = models.CharField(max_length=200, unique=False, blank=True, default=None)
    noise = models.CharField(max_length=200, unique=False, blank=True, default=None)
    width = models.CharField(max_length=200, unique=False, blank=True, default=None)
    height = models.CharField(max_length=200, unique=False, blank=True, default=None)
    length = models.CharField(max_length=200, unique=False, blank=True, default=None)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'fan'



class RigCase(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    brand = models.CharField(max_length=200, unique=False, blank=True, default=None)
    model = models.CharField(max_length=200, unique=False, blank=True, default=None)
    width = models.CharField(max_length=200, unique=False, blank=True, default=None)
    height = models.CharField(max_length=200, unique=False, blank=True, default=None)
    length = models.CharField(max_length=200, unique=False, blank=True, default=None)
    open_air = models.BooleanField()
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'rigcase'



# TODO  Price will be updated dynamically
# TODO Each GPU must have a msrp price
# https://github.com/AbenOG/skroutz_price_compare
class GPU(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    brand = models.IntegerField(choices=BRAND, default=0)
    model = models.IntegerField(choices=MODEL, default=0)
    memory = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    memory_manufacturer = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True)
    pcie_slots = models.IntegerField()
    wattage = models.ForeignKey(Wattage, on_delete=models.CASCADE, blank=True, default=None, null=True)
    comments = models.CharField(max_length=200, unique=False, blank=True, default=None, null=True )
    overclock = models.ForeignKey(Overclock, on_delete=models.CASCADE, blank=True, default=None,  null=True )
    live_price = models.ForeignKey(Price, on_delete=models.CASCADE, blank=True, default=None,  null=True )
    price = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    used_in_rig = models.ForeignKey(MiningRig, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        managed = True
        db_table = 'gpu'

    def __str__(self):
        return self.name


class Coin(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)
    price = models.FloatField()
    currency = models.CharField(max_length=200, unique=False, blank=True, default=None)
    live_price = models.ForeignKey(Price, on_delete=models.CASCADE, blank=True, default=None, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'coin'


# Value is hash / second
class Hashrate(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, blank=True, default=None, null=True)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, blank=True, default=None, null=True)
    value = models.FloatField()

    class Meta:
        managed = True
        db_table = 'hashrate'


class OperationCenter(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'operationcenter'


class ProfitabilityExperiment(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'profitabilityexperiment'


class ProfitabilityForecast(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True, default=None)
    slug = models.SlugField(max_length=200, unique=False, blank=True, default=None)
    name = models.CharField(max_length=200, unique=False, blank=True, default=None)

    class Meta:
        managed = True
        db_table = 'profitabilityforecast'


