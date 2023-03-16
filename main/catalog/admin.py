from django.contrib import admin
from .models import Supplier, Customer, Payment, Product, Order, Review, Cart#,Category
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Review)
