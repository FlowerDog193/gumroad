from django.views import generic
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(generic.ListView):
    template_name = "discover.html"
    queryset = Product.objects.all()


class ProductDetailView(generic.DetailView):
    template_name = "products/product.html"
    queryset = Product.objects.all()
    queryset_object_name = "product"


class UserProductListView(LoginRequiredMixin, generic.ListView):
    template_name = "products.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
