from django.shortcuts import redirect,render

from ecommerce.api.bankingInfo import addPaymentInfoBuyer
from ...models.paymentInfo import PaymentInfo
from ..forms.bankingForm import BankingBuyerForm, BankingSellerForm
from ...api.account_context import *

def addBankingInfo(request):
    """
    Add Banking info for the currently logged in Seller or Buyer
    """
    
    if request.session['is_seller']:
        return addBankingInfoSeller(request)
    else:
        return addBankingInfoBuyer(request)

def addBankingInfoBuyer(request):
    """
    
    """

    if request.method == "POST":
        
        payment_form = BankingBuyerForm(request.POST)

        if payment_form.is_valid():
            
            redir=redirect('home')
            status = AccountContext().refresh_id_token(request,redir)

            if status is False:
                return redirect('logout')
            elif status is redir:
                token = request.COOKIES.get('refreshToken',None)
                current_user = AccountContext().get_account_from_refresh_token(token)
            else:
                token = request.COOKIES.get('idToken',None)
                current_user = AccountContext().get_account_info(token)
            
            paymentData = payment_form.cleaned_data
            addPaymentInfoBuyer(current_user['users'][0]['email'],paymentData['firstname'],paymentData['lastname'],paymentData['number'],paymentData['expirationDate'],paymentData['cvv'])

            return redirect('home')

    else:
        payment_form = BankingBuyerForm()
    return render(request,'addBankingInfo.html',{"paymentForm":payment_form})


def addBankingInfoSeller(request):
    """
    
    """

    if request.method == "POST":
        
        payment_form = BankingSellerForm(request.POST)

        if payment_form.is_valid():
            
            redir=redirect('home')
            status = AccountContext().refresh_id_token(request,redir)

            if status is False:
                return redirect('logout')
            elif status is redir:
                token = request.COOKIES.get('refreshToken',None)
                current_user = AccountContext().get_account_from_refresh_token(token)
            else:
                token = request.COOKIES.get('idToken',None)
                current_user = AccountContext().get_account_info(token)
            
            PaymentInfo(email=current_user['users'][0]['email'],seller_payment_data=payment_form.cleaned_data).save()

            return redirect('home')

    else:
        payment_form = BankingSellerForm()
    return render(request,'addBankingInfo.html',{"paymentForm":payment_form})
    

