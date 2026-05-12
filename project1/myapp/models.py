from django.db import models

class FoodDelivery_DB(models.Model):
    Order_ID = models.IntegerField(primary_key=True)
    CustomerName = models.CharField(max_length=30)
    OrderDate = models.DateField()
    ItemName = models.CharField(max_length=100)
    OrderQty = models.IntegerField()
    UnitPrice = models.FloatField()
    TotalAmount = models.FloatField()
    DeliveryAddress = models.CharField(max_length=200)

    def __str__(self):
        return str(self.Order_ID)

