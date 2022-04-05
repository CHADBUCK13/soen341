import imp
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ecommerce.controllers.shopping_cart.orderViews import cancelOrder, orders
from .controllers.item_browsing.item_browsingViews import addItem, searchItems
from .controllers.banking.bankingViews import addBankingInfo
from .views import home
from .controllers.account.accountViews import signupBuyer,signupSeller,login,logout,resetPassword
from .controllers.shopping_cart.shopping_cartViews import *


urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("resetP/",resetPassword,name="resetPassword"),
    path("logout/",logout, name="logout"),
    path("signupB/",signupBuyer,name="signupBuyer"),
    path("signupS/",signupSeller,name="signupSeller"),
    path("addItem/",addItem, name="addItem"),
    path('searchItems/',searchItems, name="searchItems"),
    path("shopping_cart/", shopCart, name="shopping_cart"),
    path("addCartItem/", addToCart, name="addToCart"),
    path("changeAmount/",changeAmount, name="changeAmount"),
    path('deletedFromCart/',removeFromCart, name="deleteFromCart"),
    path('checkout/',checkout,name='checkout'),
    #add/remove
    path('banking/',addBankingInfo, name="addBankingInfo"),
    path('orders/', orders, name="orders"),
    path('cancelOrders/', cancelOrder, name="cancelOrder")
]

urlpatterns += staticfiles_urlpatterns()
