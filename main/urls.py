from django.urls import path
from main.views import show_main, create_products, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_products
from main.views import delete_products
from main.views import add_products_entry_ajax
from main.views import edit_products_ajax
from main.views import delete_products_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products/', create_products, name='create_products'),
    path('products/<int:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:products_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<int:id>/edit', edit_products, name='edit_products'),
    path('products/<int:id>/delete', delete_products, name='delete_products'),
    path('create-products-ajax', add_products_entry_ajax, name='add_products_entry_ajax'),
    path('products/<int:id>/edit-ajax/', edit_products_ajax, name='edit_products_ajax'),
    path('products/<int:id>/delete-ajax/', delete_products_ajax, name='delete_products_ajax'), 
]