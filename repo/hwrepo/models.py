# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
"""
MariaDB [rex]> desc leaseweb;
+----------------------------+-------------+------+-----+---------+-------+
| Field                      | Type        | Null | Key | Default | Extra |
+----------------------------+-------------+------+-----+---------+-------+
| id                         | int(11)     | NO   | PRI | NULL    |       |
| assetId                    | int(11)     | YES  |     | NULL    |       |
| location_site              | varchar(6)  | YES  |     | NULL    |       |
| location_suite             | varchar(10) | YES  |     | NULL    |       |
| location_rack              | varchar(11) | YES  |     | NULL    |       |
| location_unit              | varchar(11) | YES  |     | NULL    |       |
| specs_brand                | varchar(10) | YES  |     | NULL    |       |
| specs_chassis              | text        | YES  |     | NULL    |       |
| specs_hardwareRaidCapable  | varchar(4)  | YES  |     | NULL    |       |
| specs_cpu_type             | varchar(40) | YES  |     | NULL    |       |
| specs_cpu_quantity         | int(11)     | YES  |     | NULL    |       |
| specs_ram_size             | int(11)     | YES  |     | 0       |       |
| specs_ram_unit             | varchar(2)  | YES  |     | NULL    |       |
| serialNumber               | varchar(32) | YES  |     | NULL    |       |
| contract_id                | varchar(32) | YES  |     | NULL    |       |
| contract_customerId        | int(11)     | YES  |     | NULL    |       |
| contract_salesOrgId        | int(11)     | YES  |     | NULL    |       |
| contract_deliveryStatus    | varchar(16) | YES  |     | NULL    |       |
| contract_reference         | varchar(40) | YES  |     | NULL    |       |
| contract_internalReference | varchar(16) | YES  |     | NULL    |       |
| contract_startsAt          | datetime    | YES  |     | NULL    |       |
| contract_sla               | varchar(40) | YES  |     | NULL    |       |
| contract_contractTerm      | int(11)     | YES  |     | NULL    |       |
| contract_billingCycle      | int(11)     | YES  |     | NULL    |       |
| contract_billingFrequency  | varchar(5)  | YES  |     | NULL    |       |
| contract_pricePerFrequency | double      | YES  |     | NULL    |       |
| contract_currency          | varchar(3)  | YES  |     | NULL    |       |
| networkInterfaces          | text        | NO   |     | NULL    |       |
+----------------------------+-------------+------+-----+---------+-------+
"""


class Leaseweb(models.Model):
    assetId = models.IntegerField()
    location_site = models.CharField(max_length=6)
    location_suite = models.CharField(max_length=10)
    location_rack = models.CharField(max_length=11)
    location_unit = models.CharField(max_length=11)
    specs_brand = models.CharField(max_length=10)
    specs_chassis = models.TextField()
    specs_hardwareRaidCapable = models.CharField(max_length=4)
    specs_cpu_type = models.CharField(max_length=40)
    specs_cpu_quantity = models.IntegerField()
    specs_ram_size = models.IntegerField()
    specs_ram_unit = models.CharField(max_length=2)
    serialNumber = models.CharField(max_length=32)
    contract_id = models.CharField(max_length=32)
    contract_customerId = models.IntegerField()
    contract_salesOrgId = models.IntegerField()
    contract_deliveryStatus = models.CharField(max_length=16)
    contract_reference = models.CharField(max_length=40)
    contract_internalReference = models.CharField(max_length=16)
    contract_startsAt = models.DateTimeField()
    contract_sla = models.CharField(max_length=40)
    contract_contractTerm = models.IntegerField()
    contract_billingCycle = models.IntegerField()
    contract_billingFrequency = models.CharField(max_length=5)
    contract_pricePerFrequency = models.FloatField()
    contract_currency = models.CharField(max_length=3)
    networkInterfaces = models.TextField()
