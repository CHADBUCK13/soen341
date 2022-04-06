"""
This module contains all the logic required the item browsing views
"""

from django.shortcuts import redirect, render
from ecommerce.api.banking_info import has_payment_info
from ecommerce.api.storage import store_image
from ecommerce.api.item_browsing import get_items_by_search, add_items, get_item_by_id
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info, refresh_id_token
from ..forms.item_form import ItemForm
from ecommerce.models.items import Item
from ...views import home

def add_item(request):
    """
    Add an Item to Sell as a Seller.
    """

    if request.method=="POST":

        item_form = ItemForm(request.POST,request.FILES)

        if item_form.is_valid():

            redir=redirect('home')
            status = refresh_id_token(request,redir)

            if status is False:
                return redirect('logout')
            if status is redir:
                token = request.COOKIES.get('refreshToken',None)
                current_user = get_account_from_refresh_token(token)
            else:
                token = request.COOKIES.get('idToken',None)
                current_user = get_account_info(token)

            if has_payment_info(current_user['users'][0]['email']):

                # Save the Image File into the DB Storage
                image_url=store_image(request.FILES.get('image',None),item_form.data['name'])

                item = Item(add_item_form_data=item_form.data,
                seller_id=current_user['users'][0]['email'],
                photo=image_url)
                add_items(item)

                return redirect('home')

            item_form.add_error("Please Update your Payment Information before Adding Items for Sale.")
    else:
        item_form = ItemForm()

    return render(request,'add_item.html',{"itemForm":item_form})


def search_items(request):
    """
    Search for specific items
    """

    if request.method == "POST":

        # Get the search Keyword
        search_text = request.POST['searchText']

        # If no keyword was given, return to home
        if search_text == "":
            return home(request)

        # Get items that match that keyword
        items = get_items_by_search(search_text=search_text)

        # Inform user that no items were found
        if len(items) == 0:
            search_text = "No Items Found for: '"+search_text+"'"
        else:
            search_text = "Items Found for: '"+search_text+"'"

        return render(request,'home.html',{'items':items,'category':search_text})
    else:
        return home(request)

def get_item_description(request):
    """
    Returns item based on posted id from html
    """

    if request.method == "POST":

        # Get the itemID
        item_id = request.POST["itemID"]

        # Get items that match that keyword
        item = get_item_by_id(item_id=item_id)

        return render(request, "itemDescription.html", {"item": item})
    
    return home(request)
