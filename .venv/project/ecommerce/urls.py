"""Contains the URLs for the webiste functionalities
"""
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from .controllers.shoppingCart.order_views import cancel_an_order, orders
from .controllers.banking.banking_views import add_banking_info
from .controllers.itemBrowsing.item_browsing_views import add_item,\
    get_item_description, search_items
from .views import home
from .controllers.account.account_views import signup_buyer,signup_seller,login,\
    logout,reset_password
from .controllers.shoppingCart.shopping_cart_views import shop_cart, add_to_cart,\
    change_amount, checkout, remove_from_cart


urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("resetP/",reset_password,name="resetPassword"),
    path("logout/",logout, name="logout"),
    path("signupB/",signup_buyer,name="signupBuyer"),
    path("signupS/",signup_seller,name="signupSeller"),
    path("addItem/",add_item, name="addItem"),
    path('searchItems/',search_items, name="searchItems"),
    path("shoppingCart/", shop_cart, name="shopping_cart"),
    path("addCartItem/", add_to_cart, name="addToCart"),
    path("changeAmount/",change_amount, name="changeAmount"),
    path('deletedFromCart/',remove_from_cart, name="deleteFromCart"),
    path('checkout/',checkout,name='checkout'),
    path('banking/',add_banking_info, name="addBankingInfo"),
    path('orders/', orders, name="orders"),
    path('cancelOrders/', cancel_an_order, name="cancelOrder"),
    path('getItemDescription/', get_item_description, name="getItemDescription")
]

urlpatterns += staticfiles_urlpatterns()
