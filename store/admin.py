from django.contrib import admin
from store.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("name", )}
     
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)