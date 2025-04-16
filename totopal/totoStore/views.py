from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    products = Product.objects.prefetch_related('media').all()
    
    # Pre-process each product's media for unique colors
    for product in products:
        used_colors = []
        for media in product.media.all():
            if media.color and media.color not in used_colors:
                used_colors.append(media.color)
        product.used_colors = used_colors
    
    return render(request, 'store/home.html', {'products': products})

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def add_to_cart(request, product):
    session_key = get_session_key(request)
    product = get_object_or_404(Product, product)
    cart_item, created = CartItem.objects.get_or_create(session_key=session_key)

    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')

def view_cart(request):
    session_key = get_session_key(request)
    cart_items = CartItem.objects.filter(session_key=session_key)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

@csrf_protect
def checkout(request):
    session_key = get_session_key(request)
    cart_items = CartItem.objects.filter(session_key=session_key)

    if request.method == 'POST':
        # Collect the form data
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pay_now = 'pay_now' in request.POST  

        # Save order to the database
        Order.objects.create(
            session_key=session_key,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            pay_now=pay_now
        )

        #Clear the cart after checkout
        cart_items.delete()

        return redirect('checkout_success')

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items
    })

def checkout_success(request):
    return render(request, 'store/checkout_success.html')