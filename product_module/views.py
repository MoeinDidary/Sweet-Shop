# views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from product_module.models import Product, ProductCategory


class CategoryProductListView(ListView):
    model = Product
    template_name = 'product_module/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(ProductCategory, url_title=self.kwargs['category'])
        return Product.objects.filter(category=category, is_active=True, is_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(ProductCategory, url_title=self.kwargs['category'])
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(is_active=True, is_delete=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)
        return context


from django.shortcuts import redirect
from django.views.generic import DetailView
from .models import Product, ProductCategory, ProductComment
from .forms import ProductCommentForm


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_module/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True, is_delete=False)
        context['comments'] = self.object.comments.filter(is_active=True)
        context['form'] = ProductCommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ProductCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.user = request.user
            comment.save()
            return redirect(self.object.get_absolute_url())
        context = self.get_context_data(object=self.object)
        context['form'] = form
        return self.render_to_response(context)
