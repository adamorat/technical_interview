from django.urls import path

from star_wars.users.views import RegisterUserView, LoginUserView, LogOutView

app_name = "users"
urlpatterns = [
    path("register/", view=RegisterUserView.as_view(), name='register'),
    path("login/", view=LoginUserView.as_view(), name='login'),
    path("logout/", view=LogOutView.as_view(), name='logout')
]
