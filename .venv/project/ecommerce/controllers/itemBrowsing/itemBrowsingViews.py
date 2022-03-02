from email import message
from lib2to3.pgen2 import token
from django.shortcuts import redirect, render
from ...databaseContext import DatabaseContext
from ..forms.itemForm import ItemForm
from ...models.items import Item
from ..account import accountViews

def addItem(request):
    """
    Add an Item to Sell as a Seller.
    """

    if request.method=="POST":
        
        item_form = ItemForm(request.POST,request.FILES)

        if item_form.is_valid():

            redir=redirect('home')
            status = DatabaseContext().refresh_idToken(request,redir)

            if status is False:
                return redirect('logout')
            elif status is redir:
                token = request.COOKIES.get('refreshToken',None)
                current_user = DatabaseContext().get_account_from_refreshToken(token)
            else:
                token = request.COOKIES.get('idToken',None)
                current_user = DatabaseContext().get_account_info(token)
            
            Item(add_item_form_data=item_form.data,sellerID=current_user['users'][0]['email']).save()

            return status
    else:
        item_form = ItemForm()

    return render(request,'addItem.html',{"itemForm":item_form})