from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_desc = models.TextField()
    pub_date = models.DateField()
    product_category = models.CharField(max_length=50, default="")
    product_price = models.IntegerField(default=0)
    product_img = models.ImageField(default='media/shop/images/default.jpg', upload_to='media/shop/images')

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def add_product(self, product, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    def remove_product(self, product):
        cart_item = CartItem.objects.filter(cart=self, product=product).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

    def clear_cart(self):
        self.items.all().delete()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    Price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.product_name}"

class MyModel(models.Model):
    my_field = models.DateTimeField()

    def get_db_prep_save(self, value, connection):
        if isinstance(value, datetime):
            return value  # Ensure it's correctly handled here
        return super().get_db_prep_save(value, connection)

class contact(models.Model):
    name = models.CharField(max_length=50)
    ph_no =models.IntegerField(null=True)
    Email= models.EmailField(max_length=30)
    Address= models.TextField(max_length=100)

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.order_id