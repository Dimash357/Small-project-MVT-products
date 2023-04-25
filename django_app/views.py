from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from . import models
from .forms import ProductForm
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == "GET":
        context = {}
        return render(request, 'product_create.html', context=context)
    elif request.method == "POST":
        name = request.POST.get('name', None)
        description = request.POST.get('description', "")
        price = request.POST.get('price', "")
        image = request.POST.get('image', "")
        product = models.Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image,
        )
        return redirect(reverse('product_list', args=()))


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_edit.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})
