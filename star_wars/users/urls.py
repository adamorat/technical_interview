from django.urls import path

from star_wars.users.views import RegisterUserView

app_name = "users"
urlpatterns = [
    path("register/", view=RegisterUserView.as_view(), name='register'),
]
