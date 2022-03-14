from django.shortcuts import redirect, render

from ...api.storage import store_image
from ...api import itembrowsing
from ecommerce.api.accountContext import AccountContext
from ..forms.itemForm import ItemForm
from ...models.items import Item

def addItem(request):
    """
    Add an Item to Sell as a Seller.
    """

    if request.method=="POST":
        
        item_form = ItemForm(request.POST,request.FILES)

        if item_form.is_valid():

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
            
            # Save the Image File into the DB Storage
            image_url=store_image(request.FILES.get('image',None),item_form.data['name'])

            Item(add_item_form_data=item_form.data,sellerID=current_user['users'][0]['email'],photo=image_url).save()

            return redirect('home')
    else:
        item_form = ItemForm()

    return render(request,'addItem.html',{"itemForm":item_form})


def searchItems(request):

    if request.method == "POST":

        # Get the search Keyword
        searchText = request.POST['searchText']

        # If no keyword was given, return to home
        if searchText == "":
            return render(request,'home.html')

        # Get items that match that keyword
        items = itembrowsing.get_items_by_search(searchText=searchText)

        # Inform user that no items were found
        if len(items) == 0:
            return render(request,'searchItems.html',{'searchText':searchText,'noItems':True})

        # Display found items
        return render(request,'searchItems.html',{'searchText':searchText,'items':items})

    else:
        return render(request,'home.html')

