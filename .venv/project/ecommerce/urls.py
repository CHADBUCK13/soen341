import imp
from unicodedata import name
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ecommerce.controllers.shoppingCart.orderViews import cancelOrder, orders
from .controllers.itemBrowsing.item_browsing_views import add_item, get_item_description, search_items
from .controllers.banking.bankingViews import addBankingInfo
from .views import home
from .controllers.account.accountViews import signupBuyer,signupSeller,login,logout,resetPassword
from .controllers.shoppingCart.shoppingCartViews import *


urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("resetP/",resetPassword,name="resetPassword"),
    path("logout/",logout, name="logout"),
    path("signupB/",signupBuyer,name="signupBuyer"),
    path("signupS/",signupSeller,name="signupSeller"),
    path("addItem/",add_item, name="addItem"),
    path('searchItems/',search_items, name="searchItems"),
    path("shoppingCart/", shopCart, name="shoppingCart"),
    path("addCartItem/", addToCart, name="addToCart"),
    path("changeAmount/",changeAmount, name="changeAmount"),
    path('deletedFromCart/',removeFromCart, name="deleteFromCart"),
    path('checkout/',checkout,name='checkout'),
    #add/remove
    path('banking/',addBankingInfo, name="addBankingInfo"),
    path('orders/', orders, name="orders"),
    path('cancelOrders/', cancelOrder, name="cancelOrder"),
    path('getItemDescription/', get_item_description, name="getItemDescription")
]

urlpatterns += staticfiles_urlpatterns()
