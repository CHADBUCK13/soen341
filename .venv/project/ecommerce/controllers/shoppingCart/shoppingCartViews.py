from ast import Add
from datetime import date
import uuid
from django.shortcuts import redirect, render

from ...models.order import Order

from ...api.itembrowsing import *
from ...views import home
from ...api.shoppingCart import *
from ...api.accountContext import *
from ...api.checkingOut import *
from django.forms.models import model_to_dict
from ...models.address import *

def shopCart(request):
    """
    Shows all Items currently in cart for the current user.
    """
    
    redir=redirect('home')
    status = AccountContext().refresh_idToken(request,redir)

    if status is False:
        return redirect('logout')
    elif status is redir:
        token = request.COOKIES.get('refreshToken',None)
        current_user = AccountContext().get_account_from_refreshToken(token)
    else:
        token = request.COOKIES.get('idToken',None)
        current_user = AccountContext().get_account_info(token)
    
    shoppingCartItems=get_items_from_cart(current_user['users'][0]['email'])
    cartItems = []
    for item in shoppingCartItems:
        itemV = dict()
        itemV['item']=item[0]
        itemV['quantity']=item[1]
        itemV['total']=float(item[0].price)*int(item[1])
        cartItems.append(itemV)
    #get_items_from_cart(request.session['email']) 
    #request.session['shoppingCartItems'] = [Item(example,example,example),Item(...)] # tests
    
    
    return render(request, 'shoppingCart.html',{'shoppingCartItems':cartItems})
   
def addToCart(request):
    """
    Adds an Item to the current user's cart.
    """

    if request.method == "POST":
        
        itemID = request.POST.get("item")
        
        redir=redirect('home')
        status = AccountContext().refresh_idToken(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = AccountContext().get_account_from_refreshToken(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = AccountContext().get_account_info(token)

        add_item_to_cart(current_user['users'][0]['email'],itemID,1)

    return home(request)

def changeAmount(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        newquantity = request.POST.get('newQuantity')
        itemId = request.POST.get('itemID')

        redir=redirect('home')
        status = AccountContext().refresh_idToken(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = AccountContext().get_account_from_refreshToken(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = AccountContext().get_account_info(token)

        update_item_quantity(current_user['users'][0]['email'],itemId,newquantity)

    return shopCart(request)

def removeFromCart(request):
    if request.method == "POST":
        itemId = request.POST.get('itemID')

        redir=redirect('home')
        status = AccountContext().refresh_idToken(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = AccountContext().get_account_from_refreshToken(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = AccountContext().get_account_info(token)

        delete_items_from_cart(current_user['users'][0]['email'],itemId)
    return shopCart(request)
        
def checkout(request):
    if request.method == "POST":

        redir=redirect('home')
        status = AccountContext().refresh_idToken(request,redir)

        if status is False:
            return redirect('logout')
        elif status is redir:
            token = request.COOKIES.get('refreshToken',None)
            current_user = AccountContext().get_account_from_refreshToken(token)
        else:
            token = request.COOKIES.get('idToken',None)
            current_user = AccountContext().get_account_info(token)

        user  = AccountContext().get_buyer(current_user['users'][0]['email'])
        if user is None:
            user  = AccountContext().get_seller(current_user['users'][0]['email'])

        shoppingCartItems=get_items_from_cart(current_user['users'][0]['email'])

        print(user)

        for item in shoppingCartItems:
            delete_items_from_cart(current_user['users'][0]['email'],item[0].id)
        # order = Order(
        #     subtotal=1,
        #     total=1,
        #     nOfItems=1,
        #     cancelled=False,
        #     paymentInfo=user['paymentInfo'],
        #     items=dict(),
        #     date=date.today(),
        #     time=date.today(),
        #     shippingAddress=Address(country=user['country'],city=user['city'],streetAddress=user['address'],postalCode=user['postal_code']),
        #     billingAddress=Address(country=user['country'],city=user['city'],streetAddress=user['address'],postalCode=user['postal_code']),
        #     id=uuid.uuid1())

        #check_out(current_user['users'][0]['email'],order)

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
       