from multiprocessing import context
from urllib import request
from django.shortcuts import render
from .api import item_browsing
from django.contrib import messages
#from .models import OrderItem, Order, Address
#from .forms import shopCartForm
from .api.item_browsing import get_categories, get_items_by_category, get_all_items_dict

def home(request):
    
    # Get Categories
   
    request.session['categoriesOptions'] = get_categories()

    category=""
    if request.method=="POST":
        category = request.POST.get("category")
    
    if category is None:
        category=""

    if 'is_logged_in' in request.session:
        is_logged_in = request.session['is_logged_in']
    else:
        is_logged_in = False

    request.session['is_logged_in'] = is_logged_in


    if category != "":
        items = get_items_by_category(category,100)
        if len(items) == 0:
            category = "No Items in "+category
    else:
        items = get_all_items_dict()

    request.session.modified = True

    return render(request,'home.html',{'items':items,'category':category})

    
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
