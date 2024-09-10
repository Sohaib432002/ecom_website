from django.shortcuts import render, HttpResponse, redirect
import requests
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddToCartForm, RemoveFromCartForm
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem,Order
import random as r



def update_cart_quantity(request, product_id, action):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()

    return redirect('view_cart')
@login_required(login_url='LoginPage')
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    # Get all items in the cart
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate the total price for each item and the total cart price
    total_price = 0
    product_quantity=[]
    for item in (cart_items):
        item_total = item.quantity * item.product.product_price  # Price for each CartItem
        total_price += item_total  # Add to total cart price
        product_quantity.append(item)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'quantity_item':len(product_quantity)   # Total price of the entire cart
    }
    return render(request, 'shop/cart.html',context)
@login_required(login_url='LoginPage')
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        # Get or create a cart for the user
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Check if the product is already in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1  # Increment quantity if already in cart
        cart_item.save()

        # Calculate the price
        cart_item_total_price = cart_item.quantity * product.product_price        
        # (Optional) You can store the total price in the CartItem model if you have a field for it
        """cart_item.total_price = cart_item_total_price"""
        print(cart_item_total_price)
        cart_item.save()
        
        # Redirect to the cart view or wherever you'd like after adding to cart
        return redirect('product')
 # Redirect to an appropriate page
"""@login_required(login_url='LoginPage')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get the user's cart
    cart = Cart.objects.get(user=request.user)
    
    # Find the item in the cart and remove it
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.delete()
    
    return redirect('product') """



@login_required(login_url='LoginPage')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    CartItem.objects.filter(cart=cart, product=product).delete()
    return redirect('product')
def remove_from_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)
    CartItem.objects.filter(cart=cart, product=product).delete()
    return redirect('view_cart')
# Initialize session variables
def initialize_session(request):
    if 'beauty_products' not in request.session:
        request.session['beauty_products'] = []
    if 'electronic_products' not in request.session:
        request.session['electronic_products'] = []
    if 'automobile_products' not in request.session:
        request.session['automobile_products'] = []
    if 'cloths_products' not in request.session:
        request.session['cloths_products'] = []
    if 'food_products' not in request.session:
        request.session['food_products'] = []
    if 'total_items' not in request.session:
        request.session['total_items'] = []

    # Retrieve session data
    return {
        'beauty_products': request.session.get('beauty_products', []),
        'list_electronic_products': request.session.get('electronic_products', []),
        'list_automobile_products': request.session.get('automobile_products', []),
        'list_cloths_products': request.session.get('cloths_products', []),
        'list_food_products': request.session.get('food_products', []),
        'list_total_items': request.session.get('total_items', [])
    }


def index(request):
    Products = Product.objects.all()
    

    parms = {
        'Products': Products,
        'product_desc': Product.product_desc,
        'product_name': Product.product_name,
           
    }
    return render(request, 'shop/home.html', parms)

def products(request):
    products = Product.objects.all()
    for product in products:
        product.product_img = product.product_img.url
        print(product.product_img)
    product_img_url = product.product_img.url
    if product_img_url.startswith('/media/media/media/'):
        product_img_url = product_img_url.replace('/media/media/media/', '/media/', 1)
    
    context = {
        'products': products,
        'cleaned_img_url': product_img_url,
    }
    return render(request, 'shop/products.html', context)

def support(request):
    return render(request, 'shop/support.html')

@login_required(login_url='LoginPage')
def Tracker(request):
    return render(request, 'shop/traker.html')



def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return render(request, 'shop/contact.html')

def skiping(request):
    return render(request, 'shop/skiping.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def placeorder(request):
    cart = get_object_or_404(Cart, user=request.user)
    
    # Get all items in the cart
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Calculate the total price for each item and the total cart price
    total_price = 0
    product_quantity=[]
    for item in (cart_items):
        item_total = item.quantity * item.product.product_price  # Price for each CartItem
        total_price += item_total  # Add to total cart price
        product_quantity.append(item)
    random_number = r.randint(1000000, 9999999)  
    print(random_number)
    
    return render(request, 'shop/order_placed.html',{'total_price': total_price,'quantity_item':len(product_quantity),'order_id':random_number})


def track_order(request):
    order_id = request.GET.get('order_id')
    print(order_id)
    if order_id:
        order = get_object_or_404(Order, order_id=order_id)
        return render(request, 'track_order.html', {'order': order})
    return render(request, 'shop/traker.html', {'error': 'Order ID is required'})

    