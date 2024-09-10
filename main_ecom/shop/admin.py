from django.contrib import admindocs,admin
from .models import Product, Cart, CartItem,contact

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(contact)