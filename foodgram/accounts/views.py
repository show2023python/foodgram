from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from boards.models import Products
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'
    model = Products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.GET.get('user_name', '')
        context['product_store_name'] = self.request.GET.get('product_store_name', '')
        context['product_kinds'] = self.request.GET.get('product_kinds', '')
        context['product_place_prefecture'] = self.request.GET.get('product_place_prefecture', '')
        return context



class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm
    success_url = reverse_lazy('accounts:user_login')


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    pass
