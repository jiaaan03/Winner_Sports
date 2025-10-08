from django.forms import ModelForm
from main.models import Products
from django.utils.html import strip_tags

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured", "brand"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
