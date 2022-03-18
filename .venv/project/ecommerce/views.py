from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .api import itembrowsing
from django.contrib import messages
#from .models import OrderItem, Order, Address
#from .forms import shopCartForm

def home(request):
    
    # Get Categories
    categoriesOptions = ['Phones','Food','Games']
    request.session['categoriesOptions'] = itembrowsing.get_categories()


    categorySearch=""

    if request.method=="POST":
        categorySearch = request.POST.get("category")   


    request.session['search'] = categorySearch

    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False
    request.session['is_logged_in'] = is_logged_in


    if categorySearch != "":
        request.session['items'] = itembrowsing.get_items_by_category(categorySearch,100)
    else:
        request.session['items'] = itembrowsing.get_all_items(100)

    request.session.modified = True

    return render(request,'home.html')



    #request.session['shoppingCartItems'] = get_items_from_cart(request.session['email']) 
    request.session['shoppingCartItems'] = [Item(Banana,1,2)]
    return render(request, 'shoppingCart.html')
    
def addToCart():
    """
    Increament the number of an item
    """
    if request.method == "POST":

     if order.items().exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("shopCart")
def removeSingleItemFromCart():
    if order.items().exists():
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                order.items.remove(order_item)
            return redirect("shopCart")

def checkout():
    pass
    

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