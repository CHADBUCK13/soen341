import imp
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ecommerce.controllers.shoppingCart.orderViews import cancelOrder, orders
from .controllers.itemBrowsing.itemBrowsingViews import add_item, searchItems
from .controllers.banking.banking_views import add_banking_info
from .views import home
from .controllers.account.account_views import signup_buyer,signup_seller,login,logout,reset_password
from .controllers.shoppingCart.shoppingCartViews import *


urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("resetP/",reset_password,name="resetPassword"),
    path("logout/",logout, name="logout"),
    path("signupB/",signup_buyer,name="signupBuyer"),
    path("signupS/",signup_seller,name="signupSeller"),
    path("addItem/",add_item, name="addItem"),
    path('searchItems/',searchItems, name="searchItems"),
    path("shopping_cart/", shopCart, name="shopping_cart"),
    path("addCartItem/", addToCart, name="addToCart"),
    path("changeAmount/",changeAmount, name="changeAmount"),
    path('deletedFromCart/',removeFromCart, name="deleteFromCart"),
    path('checkout/',checkout,name='checkout'),
    path('banking/',add_banking_info, name="addBankingInfo"),
    path('orders/', orders, name="orders"),
    path('cancelOrders/', cancelOrder, name="cancelOrder")
]

urlpatterns += staticfiles_urlpatterns()
