from django.contrib import admin
from products.models import *

class CategoryInLine(admin.TabularInline):
	model=Category
	extra=1

class IdentificationInLine(admin.TabularInline):
	model=Identification
	extra=1

class MarketInterestInLine(admin.TabularInline):
	model=MarketInterest
	extra=1

class FeatureInteractionOfInLine(admin.TabularInline):
	model=FeatureInteraction
	fk_name='of'
	extra=1

class FeatureInteractionFactorInInLine(admin.TabularInline):
	model=FeatureInteraction
	fk_name='factorIn'
	extra=1

class FeatureApplicabilityInLine(admin.TabularInline):
	model=FeatureApplicability
	extra=1

class CategoryTypeInLine(admin.TabularInline):
	model=CategoryType
	extra=1

class UnitOfMeasureConversionInLine(admin.TabularInline):
	model=UnitOfMeasureConversion
	extra=1
	fk_name='convertFrom'

class SupplierProductInLine(admin.TabularInline):
	model=SupplierProduct
	extra=1

class ReorderGuidelineInLine(admin.TabularInline):
	model=ReorderGuideline
	extra=1

class ServiceAdmin( admin.ModelAdmin):
	inlines=[ CategoryInLine, FeatureApplicabilityInLine, SupplierProductInLine]

class GoodAdmin( admin.ModelAdmin):
	inlines=[ CategoryInLine, IdentificationInLine,FeatureApplicabilityInLine, SupplierProductInLine, ReorderGuidelineInLine  ]

class CategoryTypeAdmin( admin.ModelAdmin):
	inlines=[ MarketInterestInLine, CategoryTypeInLine]

class FeatureAdmin( admin.ModelAdmin):
	inlines=[ FeatureInteractionOfInLine, FeatureInteractionFactorInInLine]

class UnitOfMeasureAdmin( admin.ModelAdmin):
	inlines=[ UnitOfMeasureConversionInLine ]

admin.site.register( Service, ServiceAdmin)
admin.site.register( Good, GoodAdmin )
admin.site.register( CategoryType, CategoryTypeAdmin )
admin.site.register( Feature,  FeatureAdmin)
admin.site.register( IdentificationType )
admin.site.register( FeatureCategory )
admin.site.register( FeatureInteraction )
admin.site.register( Dimension )
admin.site.register( UnitOfMeasure, UnitOfMeasureAdmin )
admin.site.register( UnitOfMeasureConversion )
