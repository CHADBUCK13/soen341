"""
This module contains all the logic required the banking views
"""

from django.shortcuts import redirect,render
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info, refresh_id_token
from ecommerce.api.banking_info import add_payment_info_buyer, add_payment_info_seller
from ecommerce.controllers.forms.banking_form import BankingBuyerForm, BankingSellerForm

def add_banking_info(request):
    """
    Add Banking info for the currently logged in Seller or Buyer
    """

    if request.session['is_seller']:
        return add_banking_info_seller(request)
    return add_banking_info_buyer(request)

def add_banking_info_buyer(request):
    """
    Add Banking info for the currently logged in Buyer
    """

    if request.method == "POST":

        payment_form = BankingBuyerForm(request.POST)

        if payment_form.is_valid():

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

            payment_data = payment_form.cleaned_data
            add_payment_info_buyer(email=current_user['users'][0]['email'],
            first_name=payment_data['firstname'],
            last_name=payment_data['lastname'],
            number=payment_data['number'],
            expiration_date=payment_data['expirationDate'],
            cvv=payment_data['cvv'])

            return redirect('home')

    else:
        payment_form = BankingBuyerForm()
    return render(request,'add_banking_info.html',{"paymentForm":payment_form})


def add_banking_info_seller(request):
    """
    Add Banking info for the currently logged in Seller
    """

    if request.method == "POST":

        payment_form = BankingSellerForm(request.POST)

        if payment_form.is_valid():

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

            payment_data = payment_form.cleaned_data
            add_payment_info_seller(email=current_user['users'][0]['email'],
            transit=payment_data['transit'],
            institution=payment_data['institution'],
            account=payment_data['account'])

            return redirect('home')

    else:
        payment_form = BankingSellerForm()
    return render(request,'add_banking_info.html',{"paymentForm":payment_form})
