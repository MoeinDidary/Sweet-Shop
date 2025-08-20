from django.shortcuts import render, redirect, get_object_or_404
from product_module.models import Product


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart

    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total_price = 0

    for product in products:
        quantity = cart[str(product.id)]
        total = product.price * quantity
        total_price += total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': total
        })

    return render(request, 'order_module/cart-site.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')


def decrease_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    pid = str(product_id)
    if pid in cart:
        cart[pid] -= 1
        if cart[pid] <= 0:
            del cart[pid]
        request.session['cart'] = cart
    return redirect('view_cart')
