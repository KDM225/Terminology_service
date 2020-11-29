from django.contrib import admin
from .models import Catalog, Element, Version


@admin.register(Catalog)
class PostAdminCatalog(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description')
    list_filter = ('id', 'name', 'short_name')
    search_fields = ('id', 'name', 'description')


@admin.register(Version)
class PostAdminVersion(admin.ModelAdmin):
    list_display = ('id', 'version', 'start_date')
    list_filter = ('id', 'version', 'start_date')
    search_fields = ('id', 'version', 'start_date')


@admin.register(Element)
class PostAdminElement(admin.ModelAdmin):
    list_display = ('id', 'code_element', 'value_element')
    list_filter = ('id', 'code_element', 'value_element')
    search_fields = ('id', 'code_element', 'value_element')
