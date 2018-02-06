from django.contrib import admin
from .models import *


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 0


# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductCategory._meta.fields]
#
#     class Meta:
#         model = ProductCategory
#
# admin.site.register(ProductCategory, ProductCategoryAdmin)


class NewsAdmin (admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]
    inlines = [NewsImageInline]

    class Meta:
        model = News

admin.site.register(News, NewsAdmin)


class NewsImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in NewsImage._meta.fields]

    class Meta:
        model = NewsImage

admin.site.register(NewsImage, NewsImageAdmin)