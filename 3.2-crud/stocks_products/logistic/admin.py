from django.contrib import admin

from logistic.models import Product, Stock, StockProduct

class Productinline(admin.TabularInline):
    model = StockProduct
    extra = 0

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [
        Productinline
        ]
    list_display = ['__str__']
    search_fields = ['title', 'description']
    list_filter = ['title', 'description']


@admin.register(Stock)
class AdminStock(admin.ModelAdmin):
    inlines = [
        Productinline
        ]
    list_display = ['__str__']
    search_fields = ['address']
    list_filter = ['address']


@admin.register(StockProduct)
class AdminStockProduct(admin.ModelAdmin):
    
    list_display = ['__str__']
    search_fields = ['stock__address']
    list_filter = ['stock__address', 'product']