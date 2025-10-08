from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    products_list = Products.objects.all()
    
    if filter_type == "all":
        products_list = Products.objects.all()
    else:
        products_list = Products.objects.filter(user=request.user)
    
    pilihan_kategori = request.GET.get('category')
    pilihan_brand = request.GET.get('brand')

    if pilihan_kategori:
        products_list = products_list.filter(category=pilihan_kategori)

    if pilihan_brand:
        products_list = products_list.filter(brand=pilihan_brand)

    context = {
        'app_name' : 'Winner Sports',
        'name': request.user.username,
        'class': 'PBP C',
        'products_list': products_list,
        'categories': Products.CATEGORY_CHOICES,
        'brands': Products.BRAND_CHOICES,
        'selected_category': pilihan_kategori,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

@login_required(login_url='/login')
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
    data = [
        {
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'is_featured': products.is_featured,
            'brand': products.brand,
            'price': products.price,
            'id': products.pk,
            'user_id': products.user.pk if products.user else None,
        }
        for products in products_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, products_id):
    try: 
        products_item = Products.objects.filter(pk=products_id)
        xml_data = serializers.serialize("xml", products_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, products_id):
    try:
        products = Products.objects.select_related('user').get(pk=products_id)
        data = {
            'name': products.name,
            'description': products.description,
            'category': products.category,
            'thumbnail': products.thumbnail,
            'is_featured': products.is_featured,
            'brand': products.brand,
            'price': products.price,
        }
        return JsonResponse(data, safe=False)
    except Products.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'success', 'message': 'Account created successfully! Please log in.'})
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response_data = {
                    'status': 'success', 
                    'message': 'Login successful!',
                    'redirect_url': reverse('main:show_main')
                }
                return JsonResponse(response_data)
            response = redirect('main:show_main')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'Invalid username or password.'}, status=400)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_products(request, id):
    products = get_object_or_404(Products, pk=id)
    form = ProductsForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

def delete_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_products_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user
    brand = request.POST.get("brand")
    price = request.POST.get("price")

    new_products = Products(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        brand=brand,
        price=price,
    )
    new_products.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_products_ajax(request, id):
    try:
        products = Products.objects.get(pk=id)
        if products.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)

        products.name = strip_tags(request.POST.get("name"))
        products.description = strip_tags(request.POST.get("description"))
        products.category = request.POST.get("category")
        products.thumbnail = request.POST.get("thumbnail")
        products.is_featured = request.POST.get("is_featured") == 'on'
        products.brand = request.POST.get("brand")
        products.price = request.POST.get("price")
        
        products.save()
        return JsonResponse({'status': 'success', 'message': 'Product updated successfully.'})
    
    except Products.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
@csrf_exempt
@require_POST
def delete_products_ajax(request, id):
    try:
        product = Products.objects.get(pk=id)
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Permission denied'}, status=403)
        
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
    except Products.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)