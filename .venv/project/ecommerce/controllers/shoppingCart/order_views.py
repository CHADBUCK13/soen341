"""
This module contains all the logic required the order views
"""

from django.shortcuts import redirect, render
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info,\
    refresh_id_token
from ecommerce.api.checking_out import cancel_order, get_orders


def orders(request):
    """
    Gets and shows all the current orders
    """
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

    user_orders = get_orders(current_user['users'][0]['email'], 5)

    return render(request, 'orders.html', {'orders': user_orders})

def cancel_an_order(request):
    """
    Cancels a current order
    """
    if request.method == "POST":
        item_id = request.POST.get('orderID')

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

        cancel_order(current_user['users'][0]['email'], item_id)

    return orders(request)
