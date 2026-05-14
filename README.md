# Ex01 Django ORM Web Application

**Date:** 25/11/2025

---

## AIM

To develop a Django Application to store and retrieve data from an E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping (ORM).

---

## DESIGN STEPS

### STEP 1
Clone the project from GitHub.

### STEP 2
Create a new app in the Django project.

### STEP 3
Enter the code for `admin.py` and `models.py`.

### STEP 4
Detect changes and create migration files that describe how to modify the database schema.

### STEP 5
Execute the migration files and update the database schema to match the Django models.

### STEP 6
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7
Apply the migration files of the created app to the database.

### STEP 8
Execute Django admin using localhost and create details for 10 entries.

---

# PROGRAM

## models.py

```python
from django.db import models
from django.contrib import admin

class Product(models.Model):
    serialNo = models.CharField(primary_key=True, max_length=8)
    ProductName = models.CharField(max_length=30)
    ManufactureDate = models.DateTimeField()
    Price = models.IntegerField()
    Quantity = models.IntegerField()

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "serialNo",
        "ProductName",
        "ManufactureDate",
        "Price",
        "Quantity"
    ]
```

---

## admin.py

```python
from django.contrib import admin
from .models import Product, ProductAdmin

admin.site.register(Product, ProductAdmin)
```

---

# OUTPUT

![Output](output.png)

---

# RESULT

Thus, the program for creating an E-Commerce website database using Django ORM has been executed successfully.
