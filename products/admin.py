from django.contrib import admin
from products.models import *

class ProductCategoryInLine(admin.TabularInline):
	model=ProductCategory
	extra=1

class ServiceAdmin( admin.ModelAdmin):
	inlines=[ ProductCategoryInLine]

class GoodAdmin( admin.ModelAdmin):
	inlines=[ ProductCategoryInLine]

class MarketInterestInLine(admin.TabularInline):
	model=MarketInterest
	extra=1

class ProductCategoryTypeInLine(admin.TabularInline):
	model=ProductCategoryType
	extra=1

class ProductCategoryTypeAdmin( admin.ModelAdmin):
	inlines=[ MarketInterestInLine, ProductCategoryTypeInLine]

admin.site.register( Service, ServiceAdmin)
admin.site.register( Good, GoodAdmin )
admin.site.register( ProductCategoryType, ProductCategoryTypeAdmin )
