from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    products_list = Products.objects.all()
    pilihan_kategori = request.GET.get('category')
    pilihan_brand = request.GET.get('brand')

    if pilihan_kategori:
        products_list = products_list.filter(category=pilihan_kategori)

    if pilihan_brand:
        products_list = products_list.filter(brand=pilihan_brand)

    context = {
        'app_name' : 'Winner Sports',
        'name': 'Jihan Andita Kresnaputri',
        'class': 'PBP C',
        'products_list': products_list,
        'categories': Products.CATEGORY_CHOICES,
        'brands': Products.BRAND_CHOICES,
        'selected_category': pilihan_kategori,
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

def show_products(request, id):
    products = get_object_or_404(Products, pk=id)

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

def show_xml(request):
     products_list = Products.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, products_id):
    try: 
        products_item = Products.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, products_id):
    try:
        products_item = Products.objects.get(pk=products_id)
        json_data = serializers.serialize("json", [products_item])
        return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
        return HttpResponse(status=404)