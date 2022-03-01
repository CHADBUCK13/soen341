from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home
from .controllers.account.accountViews import signupBuyer,signupSeller,login,logout

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("logout/",logout, name="logout"),
    path("signupB/",signupBuyer,name="signupBuyer"),
    path("signupS/",signupSeller,name="signupSeller")
]

urlpatterns += staticfiles_urlpatterns()
