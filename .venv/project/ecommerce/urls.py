from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .controllers.itemBrowsing.itemBrowsingViews import addItem, searchItems
from .controllers.banking.bankingViews import addBankingInfo
from .views import home
from .controllers.account.accountViews import signupBuyer,signupSeller,login,logout,resetPassword

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
    path('banking/',addBankingInfo, name="addBankingInfo")
]

urlpatterns += staticfiles_urlpatterns()
