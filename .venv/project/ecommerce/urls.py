from django.urls import path
from .views import home
from .controllers.account.accountViews import signup, signupBuyer,signupSeller,login,logout

urlpatterns = [
    path(r'^$', home, name="home"),
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("logout/",logout, name="logout"),
    path("signupOption/", signup, name="signupOption"),
    path("signupB/",signupBuyer,name="signupBuyer"),
    path("signupS/",signupSeller,name="signupSeller")
]
