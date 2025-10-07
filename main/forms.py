from django.utils.html import strip_tags
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "thumbnail", "category", "stock", "is_featured"]     
    
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_desc(self):
        desc = self.cleaned_data["description"]
        return strip_tags(desc)
    
    def clean_thumbnail(self):
        thumbnail = self.cleaned_data["thumbnail"]
        return strip_tags(thumbnail)
    
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return strip_tags(stock)