"""
"""

from django.shortcuts import redirect,render
from ecommerce.api.banking_info import add_payment_info_buyer
from ecommerce.models.paymentInfo import PaymentInfo
from ..forms.banking_form import BankingBuyerForm, BankingSellerForm
from ecommerce.api.account_context import get_account_from_refresh_token, get_account_info, refresh_id_token

def add_banking_info(request):
    """
    Add Banking info for the currently logged in Seller or Buyer
    """
    
    if request.session['is_seller']:
        return add_banking_info_seller(request)
    else:
        return add_banking_info_buyer(request)

def add_banking_info_buyer(request):
    """
    
    """

    if request.method == "POST":
        
        payment_form = banking_buyer_form(request.POST)

        if payment_form.is_valid():
            
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
            
            paymentData = payment_form.cleaned_data
            addPaymentInfoBuyer(current_user['users'][0]['email'],paymentData['firstname'],paymentData['lastname'],paymentData['number'],paymentData['expirationDate'],paymentData['cvv'])

            return redirect('home')

    else:
        payment_form = banking_buyer_form()
    return render(request,'add_banking_info.html',{"paymentForm":payment_form})


def add_banking_info_seller(request):
    """
    
    """

    if request.method == "POST":
        
        payment_form = BankingSellerForm(request.POST)

        if payment_form.is_valid():
            
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
            
            PaymentInfo(email=current_user['users'][0]['email'],seller_payment_data=payment_form.cleaned_data).save()

            return redirect('home')

    else:
        payment_form = BankingSellerForm()
    return render(request,'add_banking_info.html',{"paymentForm":payment_form})
