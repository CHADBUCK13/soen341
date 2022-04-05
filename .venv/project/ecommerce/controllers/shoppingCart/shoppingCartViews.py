from django.shortcuts import redirect, render
from datetime import datetime
from ecommerce.controllers.forms.bankingForm import BankingBuyerForm

from ecommerce.models.order import Order

from ecommerce.api.item_browsing import *
from ...views import home
from ecommerce.api.shopping_cart import add_item_to_cart, delete_items_from_cart, get_items_from_cart, update_item_quantity
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info, get_buyer, get_seller, refresh_id_token
from ecommerce.api.checking_out import check_out, get_payment_info  
from django.forms.models import model_to_dict
from ecommerce.models.address import Address

def shopCart(request):
    """
    Shows all Items currently in cart for the current user.
    """
    
    redir=redirect('home')
    status = refresh_id_token( request,redir)

    if status is False:
        return redirect('logout')
    elif status is redir:
        token = request.COOKIES.get('refreshToken',None)
        current_user = get_account_from_refresh_token(token)
    else:
        token = request.COOKIES.get('idToken',None)
        current_user = get_account_info( token)
    
    shopping_cartItems=get_items_from_cart(current_user['users'][0]['email'])
    cartItems = []
    for item in shopping_cartItems:
        itemV = dict()
        itemV['item']=item[0]
        itemV['quantity']=item[1]
        itemV['total']=float(item[0].price)*int(item[1])
        cartItems.append(itemV)
    #get_items_from_cart(request.session['email']) 
    #request.session['shopping_cartItems'] = [Item(example,example,example),Item(...)] # tests
    
    paymentMethods = get_payment_info(current_user['users'][0]['email'])
    methods = []
    for method in paymentMethods:
        number = method.number
        method_dict = dict()
        method_dict['first'] = method.first
        method_dict['last'] = method.last
        method_dict['number'] = number[len(number) - 4: len(number)]
        method_dict['experiationDate'] = method.expiration_date
        method_dict['CVV'] = method.CVV
        method_dict['type'] = number[0]
        methods.append(method_dict)

    return render(request, 'shopping_cart.html',{'shopping_cartItems':cartItems, 'methods':methods})
   
def addToCart(request):
    """
    Adds an Item to the current user's cart.
    """

    if request.method == "POST":
        
        itemID = request.POST.get("item")
        
        redir=redirect('home')
        status = refresh_id_token(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = get_account_info(token)

        add_item_to_cart(current_user['users'][0]['email'],itemID,1)

    return home(request)

def changeAmount(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        newquantity = request.POST.get('newQuantity')
        itemId = request.POST.get('itemID')

        redir=redirect('home')
        status = refresh_id_token(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = get_account_info(token)

        update_item_quantity(current_user['users'][0]['email'],itemId,newquantity)

    return shopCart(request)

def removeFromCart(request):
    if request.method == "POST":
        itemId = request.POST.get('itemID')

        redir=redirect('home')
        status = refresh_id_token(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = get_account_info(token)

        delete_items_from_cart(current_user['users'][0]['email'],itemId)
    return shopCart(request)
        
def checkout(request):
    if request.method == "POST":

        redir=redirect('home')
        status = refresh_id_token(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = get_account_from_refresh_token(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = get_account_info(token)

        user  = get_buyer(current_user['users'][0]['email'])
        if user is None:
            user  = get_seller(current_user['users'][0]['email'])

        subtotal = 0.0
        n_of_items = 0
        payment_info = request.POST.get('number')
        shopping_cartItems=get_items_from_cart(current_user['users'][0]['email'])
        orderItems = []
        for item in shopping_cartItems:
            price = float(item[0].price)
            quantity = item[1]
            subtotal += price*float(quantity)
            n_of_items += 1
            item_dict = item[0].to_dict()
            item_dict['quantity'] = quantity
            orderItems.append(item_dict)

        order = Order(
            subtotal= subtotal,
            total= subtotal*1.15,
            n_of_items=1,
            cancelled=False,
            payment_info=payment_info,
            items=orderItems,
            date=datetime.now(),
            time=datetime.now(),
            shipping_address=Address(country=user['country'],city=user['city'],street_address=user['address'],postal_code=user['postal_code']),
            billing_address=Address(country=user['country'],city=user['city'],street_address=user['address'],postal_code=user['postal_code']))

        check_out(current_user['users'][0]['email'],order)

    return home(request)

# def get_coupon(request, code):
#     try:
#         coupon = Coupon.objects.get(code=code)
#         return coupon
#     except:
#        print("This coupon does not exist")

# class CouponView():
#     def post(self, *args, **kwargs):
#         form = CouponForm(self.request.POST or None)
#         if form.is_valid():
#             try:
#                 code = form.cleaned_data.get('code')
#                 order = Order.objects.get(
#                     user=self.request.user, ordered=False)
#                 order.coupon = get_coupon(self.request, code)
#                 order.save()
#                 messages.success(self.request, "Successfully added coupon")
#                 return redirect("core:checkout")
#             except ObjectDoesNotExist:
#                 messages.info(self.request, "You do not have an active order")
#                 return redirect("core:checkout")



#Add checkout view
#Add remove add item view(add/remove form cart)
       