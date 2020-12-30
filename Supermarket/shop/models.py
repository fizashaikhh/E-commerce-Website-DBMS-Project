# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Customer(models.Model):
    custid = models.AutoField(db_column='custID',primary_key=True)  # Field name made lowercase.
    name = models.TextField(max_length=100, blank=True, null=True)
    contact = models.TextField(max_length=100,blank=True, null=True)

    def __str__(self):
        return str(self.custid)
    class Meta:
        db_table = 'Customer'


class Category(models.Model):
    catid = models.IntegerField(db_column='catID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True,max_length=100, null=True)

    def __str__(self):
        return str(self.catid)

    class Meta:
        db_table = 'Category'




class Order(models.Model):
    orderid = models.AutoField(db_column='orderID',primary_key=True)  # Field name made lowercase.
    custid = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column="custID")  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.orderid)

    class Meta:
        db_table = 'Order'


class Product(models.Model):
    prodid = models.AutoField(db_column='prodID',primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True,max_length=100, null=True)
    unitprice = models.IntegerField(db_column='unitPrice', blank=True, null=True)  # Field name made lowercase.
    instock = models.IntegerField(db_column='inStock', blank=True, null=True)  # Field name made lowercase.
    catid = models.ForeignKey(Category,on_delete=models.CASCADE, db_column="catID")
    image = models.ImageField(upload_to='shop/images', default="0")

    def __str__(self):
        return str(self.prodid)

    class Meta:
        db_table = 'Product'

class OrderDetails(models.Model):
    id = models.AutoField(db_column="ID",primary_key=True)
    prodid = models.ForeignKey(Product , on_delete=models.CASCADE,db_column="prodID")  # Field name made lowercase.
    qty = models.IntegerField(blank=True, null=True)
    orderid = models.ForeignKey(Order,on_delete=models.CASCADE,db_column="orderID") # Field name made lowercase.

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'Order-Details'



class Supplier(models.Model):
    supid = models.AutoField(db_column='supID',primary_key=True)  # Field name made lowercase.
    catid = models.ForeignKey(Category, on_delete=models.CASCADE, db_column="catID")  # Field name made lowercase.
    name = models.TextField(blank=True, null=True,max_length=100)
    contact = models.TextField(blank=True, null=True,max_length=100)  # This field type is a guess.

    def __str__(self):
        return str(self.supid)
    class Meta:
        db_table = 'Supplier'
