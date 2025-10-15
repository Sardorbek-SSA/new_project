from django.contrib import admin
from .models import CategoryHome, Home

@admin.register(CategoryHome)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","is_active")
    list_filter = ("name","is_active")
    search_fields = ("name",)
    
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("name","price")
    list_filter = ("name","recomended")
    search_fields = ("name",)