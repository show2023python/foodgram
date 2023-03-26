from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, Http404
from django.views.generic.base import TemplateView
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy

import os
from .models import(
    Products,
)
from .forms import(
    ProductUpdateForm,
    StoreInputForm
)
from . import forms

#検索ページ用#
class ProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('boards', 'product_list.html')
    ordering = '-id'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET
        if store_name:= query.get('store_name'):
            queryset = queryset.filter(store_name__icontains=store_name)
        if kinds:= query.get('kinds'):
            queryset = queryset.filter(
                kinds__icontains=kinds
            )
        if place_prefecture:= query.get('place_prefecture'):
            queryset = queryset.filter(
                place_prefecture__icontains=place_prefecture
            )
        return queryset.exclude(user=self.request.user)

#お店情報入力#
class CreateProductView(LoginRequiredMixin, CreateView):
    model = Products
    template_name = os.path.join('boards', 'store_input.html')
    form_class = StoreInputForm
    success_url = reverse_lazy('boards:users_product_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

#更新ページ#
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = os.path.join('boards', 'update_product.html')
    form_class = ProductUpdateForm
    model = Products
    
    def get_success_url(self,  **kwargs):
       pk = self.kwargs["pk"]
       return reverse_lazy('boards:product_detail', kwargs={"pk": pk})
    # success_url = reverse_lazy('boards:product_detail')

#削除ページ#
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = os.path.join('boards', 'delete_product.html')
    model = Products
    success_url = reverse_lazy('boards:users_product_list')

#詳細ページ#
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Products
    template_name = os.path.join('boards', 'product_detail.html')

#ログインユーザーのページ#
class ProductListView_User(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('boards', 'users_product_list.html')
    def get_queryset(self):
        return Products.objects.filter(user=self.request.user)

#他のユーザーのページ#
class ProductListView_Another(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('boards', 'another_product_list.html')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data_list = Products.objects.filter(user_id=self.kwargs['pk'])
        context['product_data_list'] = data_list
        context['user__name'] = data_list[0].user.username
        return context

#すべての投稿一覧#
class AllProductListView(LoginRequiredMixin, ListView):
    model = Products
    template_name = os.path.join('boards', 'all_products_list.html')
    def get_queryset(self):
       return Products.objects.exclude(user=self.request.user)
    ordering = '-id'

