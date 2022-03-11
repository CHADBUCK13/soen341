from django.shortcuts import render

from ecommerce.api import checkingOut
from ecommerce.models.order import Order
from .api import itembrowsing

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

def test_email(request):
    if(request.Get.get('test_btn')):
        order = Order(3.00,4.00,1,False,"**********4561",{"item1":{"item_id": "1", "quantity":"1"}})
        checkingOut.send_confirmation_email("123456", order, "chadbuck31@gmail.com")
