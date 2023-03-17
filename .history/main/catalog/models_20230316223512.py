from django.db import models
from django.contrib.auth.models import User
class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

from django.db import models


#Модели таблиц

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return super().__str__()
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catalog/products/img')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.__str__()
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return super().__str__()
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ], max_length=20)
    
    def __str__(self) -> str:
        return super().__str__()
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(choices=[
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('CONFIRMATION', 'Confirmation'),
        ('ACCEPTED', 'Accepted'),
        ('CANCELLED', 'Cancelled'),
    ], max_length=20)
    date_paid = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return super().__str__()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return super().__str__()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return super().__str__()

