from django.contrib import admin
from M_t_M.models import Customer, Products




# Register your models here.
@admin.register(Customer)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'cus_name', 'cus_email', 'cus_mobile']

# admin.site.register(Products)
@admin.register(Products)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_customerName', 'pro_name', 'pro_qty']

    def get_customerName(self, obj):
        return ", ".join([c_name.cus_name for c_name in obj.cus.all()])
    
    
    get_customerName.short_description = 'Customer'






