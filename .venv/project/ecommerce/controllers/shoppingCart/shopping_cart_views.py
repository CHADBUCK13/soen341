"""
This module contains all the logic required the shopping cart views
"""
from datetime import datetime
from django.shortcuts import redirect, render
from ecommerce.models.order import Order
from ecommerce.models.address import Address
from ecommerce.api.item_browsing import *
from ecommerce.api.shopping_cart import add_item_to_cart, delete_items_from_cart,\
    get_items_from_cart, update_item_quantity
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info,\
    get_buyer, get_seller, refresh_id_token
from ecommerce.api.checking_out import check_out, get_payment_info
from ecommerce.views import home


def shop_cart(request):
    """
    Shows all Items currently in cart for the current user.
    """

    redir = redirect('home')
    status = refresh_id_token(request, redir)

    if status is False:
        return redirect('logout')
    if status is redir:
        token = request.COOKIES.get('refreshToken', None)
        current_user = get_account_from_refresh_token(token)
    else:
        token = request.COOKIES.get('idToken', None)
        current_user = get_account_info(token)

    shopping_cart_items = get_items_from_cart(
        current_user['users'][0]['email'])
    cart_items = []
    for item in shopping_cart_items:
        item_value = dict()
        item_value['item'] = item[0]
        item_value['quantity'] = item[1]
        item_value['total'] = float(item[0].price)*int(item[1])
        cart_items.append(item_value)
    # get_items_from_cart(request.session['email'])
    # request.session['shopping_cartItems'] = [Item(example,example,example),Item(...)] # tests

    payment_methods = get_payment_info(current_user['users'][0]['email'])
    methods = []
    for method in payment_methods:
        number = method.number
        method_dict = dict()
        method_dict['first'] = method.first
        method_dict['last'] = method.last
        method_dict['number'] = number[len(number) - 4: len(number)]
        method_dict['experiationDate'] = method.expiration_date
        method_dict['cvv'] = method.cvv
        method_dict['type'] = number[0]
        methods.append(method_dict)

    return render(request,'shopping_cart.html',{'shopping_cartItems':cart_items,'methods': methods})


def add_to_cart(request):
    """
    Adds an Item to the current user's cart.
    """

    if request.method == "POST":

        item_id = json.load(request)['itemID']

        redir = redirect('home')
        status = refresh_id_token(request, redir)

        if status is False:
            return redirect('logout')
        if status is redir:
            token = request.COOKIES.get('refreshToken', None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken', None)
            current_user = get_account_info(token)

        add_item_to_cart(current_user['users'][0]['email'], item_id, 1)

    return home(request)


def change_amount(request):
    """
    Change the amount for an item in the cart
    """
    if request.method == "POST":
        new_quantity = request.POST.get('newQuantity')
        item_id = request.POST.get('itemID')

        redir = redirect('home')
        status = refresh_id_token(request, redir)

        if status is False:
            return redirect('logout')
        if status is redir:
            token = request.COOKIES.get('refreshToken', None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken', None)
            current_user = get_account_info(token)

        update_item_quantity(
            current_user['users'][0]['email'], item_id, new_quantity)

    return shop_cart(request)


def remove_from_cart(request):
    """
    Removes an item from the cart
    """
    if request.method == "POST":
        item_id = request.POST.get('itemID')

        redir = redirect('home')
        status = refresh_id_token(request, redir)

        if status is False:
            return redirect('logout')
        if status is redir:
            token = request.COOKIES.get('refreshToken', None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken', None)
            current_user = get_account_info(token)

        delete_items_from_cart(current_user['users'][0]['email'], item_id)
    return shop_cart(request)


def checkout(request):
    """
    Checks out the contents of the cart and creates an order
    """
    if request.method == "POST":

        redir = redirect('home')
        status = refresh_id_token(request, redir)

        if status is False:
            return redirect('logout')
        if status is redir:
            token = request.COOKIES.get('refreshToken', None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken', None)
            current_user = get_account_info(token)

        user = get_buyer(current_user['users'][0]['email'])
        if user is None:
            user = get_seller(current_user['users'][0]['email'])

        subtotal = 0.0
        n_of_items = 0
        payment_info = request.POST.get('number')
        shopping_cart_items = get_items_from_cart(
            current_user['users'][0]['email'])
        order_items = []
        for item in shopping_cart_items:
            price = float(item[0].price)
            quantity = item[1]
            subtotal += price*float(quantity)
            n_of_items += 1
            item_dict = item[0].to_dict()
            item_dict['quantity'] = quantity
            order_items.append(item_dict)

        order = Order(
            subtotal=subtotal,
            total=subtotal*1.15,
            n_of_items=1,
            cancelled=False,
            payment_info=payment_info,
            items=order_items,
            date=datetime.now(),
            time=datetime.now(),
            shipping_address=Address(country=user['country'],
                                     city=user['city'],
                                     street_address=user['address'],
                                     postal_code=user['postal_code']),
            billing_address=Address(country=user['country'],
                                    city=user['city'],
                                    street_address=user['address'],
                                    postal_code=user['postal_code']))

        check_out(current_user['users'][0]['email'], order)

    return home(request)
