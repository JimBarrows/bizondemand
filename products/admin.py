from django.contrib import admin
from products.models import *

class ProductCategoryInLine(admin.TabularInline):
	model=ProductCategory
	extra=1

class IdentificationInLine(admin.TabularInline):
	model=Identification
	extra=1

class MarketInterestInLine(admin.TabularInline):
	model=MarketInterest
	extra=1

class ProducFeatureInteractionOfInLine(admin.TabularInline):
	model=ProductFeatureInteraction
	fk_name='of'
	extra=1

class ProducFeatureInteractionFactorInInLine(admin.TabularInline):
	model=ProductFeatureInteraction
	fk_name='factorIn'
	extra=1

class FeatureApplicabilityInLine(admin.TabularInline):
	model=ProductFeatureApplicability
	extra=1

class ProductCategoryTypeInLine(admin.TabularInline):
	model=ProductCategoryType
	extra=1

class ServiceAdmin( admin.ModelAdmin):
	inlines=[ ProductCategoryInLine, FeatureApplicabilityInLine]

class GoodAdmin( admin.ModelAdmin):
	inlines=[ ProductCategoryInLine, IdentificationInLine,FeatureApplicabilityInLine  ]

class ProductCategoryTypeAdmin( admin.ModelAdmin):
	inlines=[ MarketInterestInLine, ProductCategoryTypeInLine]

class ProductFeatureAdmin( admin.ModelAdmin):
	inlines=[ ProducFeatureInteractionOfInLine, ProducFeatureInteractionFactorInInLine]

admin.site.register( Service, ServiceAdmin)
admin.site.register( Good, GoodAdmin )
admin.site.register( ProductCategoryType, ProductCategoryTypeAdmin )
admin.site.register( ProductFeature,  ProductFeatureAdmin)
admin.site.register( IdentificationType )
admin.site.register( ProductFeatureCategory )
admin.site.register( ProductFeatureType )
admin.site.register( ProductFeatureInteraction )
