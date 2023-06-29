from django.contrib import admin
from .models import UserAuthentication, AdminProfile, Product, Category, Cart, Order


class UserAuthenticationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'surname']


# class CategoryProduct(admin.StackedInline):
#     model = ProductCategory
#     extra = 1


class ProductAdmin(admin.ModelAdmin):
    # inlines = [CategoryProduct, ]
    list_display = ['name', 'price', 'in_Stocked']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(UserAuthentication)
admin.site.register(AdminProfile)
