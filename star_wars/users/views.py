from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView

from star_wars.users.forms import UserCreationForm, UserLoginForm
from star_wars.users.mixins import NoLoginRequiredMixin


class RegisterUserView(NoLoginRequiredMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('films:index', args=())

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        authenticate(request=self.request,
                     username=form.instance.username,
                     password=form.data.get('password'))
        login(self.request, form.instance)
        return form_valid


class LoginUserView(NoLoginRequiredMixin, CreateView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('films:index', args=())

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        user = authenticate(request=self.request,
                            username=form.data.get('username'),
                            password=form.data.get('password'))
        login(self.request, user)
        return form_valid
