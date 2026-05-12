from django.contrib import admin
from .models import FoodDelivery_DB

class FoodDelivery_DBAdmin(admin.ModelAdmin):
    list_display = (
        'Order_ID', 'CustomerName', 'OrderDate', 'ItemName',
        'OrderQty', 'UnitPrice', 'TotalAmount', 'DeliveryAddress'
    )

admin.site.register(FoodDelivery_DB, FoodDelivery_DBAdmin)