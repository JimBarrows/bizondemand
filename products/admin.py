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

class InventoryItemVarianceInLine(admin.TabularInline):
	model=InventoryItemVariance
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

class InventoryItemAdmin( admin.ModelAdmin):
	inlines=[ InventoryItemVarianceInLine ]

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
admin.site.register( SerializedInventoryItem, InventoryItemAdmin )
admin.site.register( NonSerializedInventoryItem, InventoryItemAdmin )
admin.site.register( Reason )
admin.site.register( ContainerType )
admin.site.register( Container )
admin.site.register( Lot )
admin.site.register( InventoryItemStatusType )
admin.site.register( BasePrice )
admin.site.register( DiscountComponent )
admin.site.register( SurchargeComponent )
admin.site.register( ManufacturerSuggestedPrice )
admin.site.register( OneTimeCharge )
admin.site.register( RecurringCharge )
admin.site.register( UtilizationCharge )
admin.site.register( QuantityBreak )
admin.site.register( OrderValue )
admin.site.register( SaleType )
admin.site.register( TimeFrequencyMeasure )
admin.site.register( CurrencyMeasure )
