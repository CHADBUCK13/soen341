from django.shortcuts import redirect, render
from ecommerce.api.bankingInfo import hasPaymentInfo
from ecommerce.api.storage import store_image
from ecommerce.api.itembrowsing import get_items_by_search, addItems, get_item_by_ID
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info, refresh_id_token
from ..forms.itemForm import ItemForm
from ecommerce.models.items import Item
from ...views import home

def addItem(request):
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
            elif status is redir:
                token = request.COOKIES.get('refreshToken',None)
                current_user = get_account_from_refresh_token(token)
            else:
                token = request.COOKIES.get('idToken',None)
                current_user = get_account_info(token)
            
            if hasPaymentInfo(current_user['users'][0]['email']):

                # Save the Image File into the DB Storage
                image_url=store_image(request.FILES.get('image',None),item_form.data['name'])


                item = Item(add_item_form_data=item_form.data,seller_id=current_user['users'][0]['email'],photo=image_url)
                addItems(item)

                return redirect('home')
            else:
                item_form.add_error("Please Update your Payment Information before Adding Items for Sale.")
    else:
        item_form = ItemForm()

    return render(request,'addItem.html',{"itemForm":item_form})


def searchItems(request):

    if request.method == "POST":

        # Get the search Keyword
        searchText = request.POST['searchText']

        # If no keyword was given, return to home
        if searchText == "":
            return home(request)

        # Get items that match that keyword
        items = get_items_by_search(searchText=searchText)

        # Inform user that no items were found
        if len(items) == 0:
            searchText = "No Items Found for: '"+searchText+"'" 
        else:
            searchText = "Items Found for: '"+searchText+"'" 

        return render(request,'home.html',{'items':items,'category':searchText})
    else:
        return home(request)


def getItems(request):

    if request.method == "POST":

        # Get the itemID
        itemID = request.POST['itemID']

        # Get items that match that keyword
        items = get_item_by_ID(itemID=itemID)

        return render(request,'itemDescription.html',{'items':items})
    else:
        return home(request)
