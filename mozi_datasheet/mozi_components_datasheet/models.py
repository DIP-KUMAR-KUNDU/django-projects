from django.db import models
import datetime

# Create your models here.
class Item(models.Model):

    id = models.CharField(max_length=200, primary_key=True)
    img = models.ImageField(upload_to= 'pics')
    desc = models.TextField()
    stock = models.IntegerField(default=0)
    tested = models.IntegerField(default=0)
    not_tested = models.IntegerField(default=0)


class TransactionList(models.Model):

    name = models.CharField(max_length=200)
    wid_name = models.CharField(max_length=200)
    wid_time = models.DateTimeField(default= datetime.datetime.now())
    wid_quant = models.IntegerField(default=0)
    wid_purp = models.TextField()


class TransactionList1(models.Model):

    name = models.CharField(max_length=200)
    wid_name = models.CharField(max_length=200)
    wid_time = models.DateTimeField(default= datetime.datetime.now())
    wid_quant = models.IntegerField(default=0)
    wid_purp = models.TextField()