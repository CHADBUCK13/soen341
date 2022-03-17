from django.shortcuts import redirect, render
from ecommerce.api.storage import store_image
from ecommerce.api.itembrowsing import get_items_by_search, addItems
from ecommerce.api.accountContext import AccountContext
from ..forms.itemForm import ItemForm
from ecommerce.models.items import Item

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
            
            if hasPaymentInfo(current_user['users'][0]['email']):

                # Save the Image File into the DB Storage
                image_url=store_image(request.FILES.get('image',None),item_form.data['name'])


                item = Item(add_item_form_data=item_form.data,sellerID=current_user['users'][0]['email'],photo=image_url)
                addItems(item)

                return redirect('home')
            else:
                item_form.add_error(None,"Please Update your Payment Information before Adding Items for Sale.")
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
        items = get_items_by_search(searchText=searchText)

        # Inform user that no items were found
        if len(items) == 0:
            return render(request,'searchItems.html',{'searchText':searchText,'noItems':True})

        # Display found items
        return render(request,'searchItems.html',{'searchText':searchText,'items':items})

    else:
        return render(request,'home.html')

