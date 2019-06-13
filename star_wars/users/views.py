from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView

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


class LoginUserView(NoLoginRequiredMixin, FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('films:index', args=())

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        try:
            user = authenticate(request=self.request,
                                username=form.data.get('username'),
                                password=form.data.get('password'))
            login(self.request, user)
        except:
            form._errors = 'Credenciales de autenticación erroneos'
            return super().form_invalid(form)
        return form_valid


class LogOutView(LoginRequiredMixin, View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('users:login', args=()))
