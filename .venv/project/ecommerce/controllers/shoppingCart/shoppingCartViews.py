from django.shortcuts import redirect, render
from ...api.itembrowsing import *
from ...views import home

def shopCart(request):
    """
    Shows all Items currently in cart for the current user.
    """
    

    
    shoppingCartItems =  get_all_items()#get_items_from_cart(request.session['email']) 
    #request.session['shoppingCartItems'] = [Item(example,example,example),Item(...)] # tests
    
    print(shoppingCartItems)
    
    return render(request, 'shoppingCart.html',{'shoppingCartItems':shoppingCartItems})
   
def addToCart(request):
    """
    Adds an Item to the current user's cart.
    """
    print("here")
    if request.method == "POST":
        print(request.POST)
    
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
       