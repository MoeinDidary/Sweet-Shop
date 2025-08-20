from django.contrib import admin

from product_module import models

# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
