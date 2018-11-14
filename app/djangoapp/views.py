import os
from django.views import generic
from django.conf import settings
from djangoapp.models import Measurement
from djangoapp.models import Product
from django.shortcuts import render
from django.urls import reverse_lazy
from djangoapp.forms import ProductForm


class MeasurementList(generic.ListView):
    model = Measurement
    context_object_name = 'measurements'
    template_name = 'measurement_list.html'


    def get(self, request, *args, **kwargs):
        try:
            file_path = os.path.join(settings.BASE_DIR, 'test_data')
            measurement_file = open(file_path, 'r')
            for value in measurement_file:
                Measurement.objects.get_or_create(value=value)
        except IOError:
            pass

        return super(MeasurementList, self).get(request, *args, **kwargs)


class ProductList(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'


    def get(self, request, *args, **kwargs):
        return super(ProductList, self).get(request, *args, **kwargs)


class ProductCreate(generic.CreateView):
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')
