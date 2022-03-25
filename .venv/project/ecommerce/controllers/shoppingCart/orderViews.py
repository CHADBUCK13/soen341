import re
from django.shortcuts import redirect, render

from ecommerce.api.accountContext import AccountContext
from ecommerce.api.checkingOut import cancel_order, get_orders


def orders(request):
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

    orders = get_orders(current_user['users'][0]['email'], 5)

    return render(request, 'orders.html', {'orders': orders})

def cancelOrder(request):
    if request.method == "POST":
        itemId = request.POST.get('orderID')

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

        cancel_order(current_user['users'][0]['email'], itemId)

    return orders(request)