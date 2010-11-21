from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from party.models import PartyType
from datetime import datetime
from party.models import Organization, Facility, PartyRole, GeographicBoundary

class Product(PolymorphicModel):
	name = models.CharField(max_length=250)
	introductionDate = models.DateField(blank=True, null=True)
	salesDiscontinuationDate = models.DateField(blank=True, null=True)
	supportDiscontinuationDate = models.DateField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	categories = models.ManyToManyField( 'CategoryType', through='Category')
	manufacturedBy = models.ForeignKey(Organization, related_name='producerOf_set')
	suppliedThru = models.ManyToManyField( Organization, through='SupplierProduct')
	def __unicode__(self):
		return self.name

class Good(Product):
	identifiers = models.ManyToManyField( 'IdentificationType', through='Identification')
	def __unicode__(self):
		return self.name

class Service(Product):
	def __unicode__(self):
		return self.name

class PriceComponent( PolymorphicModel):
	fromDate = models.DateField()
	thruDate = models.DateField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	geographicBoundary = models.ForeignKey(GeographicBoundary, blank=True, null=True)
	partyType = models.ForeignKey(PartyType, blank=True, null=True)
	productCategory = models.ForeignKey('CategoryType', blank=True, null=True) 
	quantityBreak = models.ForeignKey('QuantityBreak', blank=True, null=True)
	orderValue = models.ForeignKey('OrderValue', blank=True, null=True)
	salesType = models.ForeignKey('SaleType', blank=True, null=True)
	pricerOf = models.ForeignKey(Organization)
	feature = models.ForeignKey('Feature', blank=True, null=True)
	product = models.ForeignKey('Product')
	currency = models.ForeignKey('CurrencyMeasure', blank=True, null=True)

class BasePrice( PriceComponent):
	''' A starting point for figuring out the price. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)

class DiscountComponent( PriceComponent):
	''' Discounts that can occur. '''
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class SurchargeComponent( PriceComponent):
	''' Discounts that can occur. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class ManufacturerSuggestedPrice( PriceComponent):
	''' Not necessarily the price being charged. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)

class OneTimeCharge( PriceComponent):
	''' Not necessarily the price being charged. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class RecurringCharge( PriceComponent):
	per = models.ForeignKey('TimeFrequencyMeasure')
	price = models.DecimalField( max_digits=8, decimal_places=2)

class UtilizationCharge( PriceComponent):
	per = models.ForeignKey('UnitOfMeasure')
	quantity = models.IntegerField()
	price = models.DecimalField( max_digits=8, decimal_places=2)

class SaleType( models.Model):
	description = models.CharField(max_length=250)

class OrderValue( models.Model):
	fromValue = models.DecimalField( max_digits=9, decimal_places=2)
	thruValue = models.DecimalField( max_digits=9, decimal_places=2)

class QuantityBreak( models.Model):
	fromQuantity = models.IntegerField()
	thruQuantity = models.IntegerField()

class InventoryItem( PolymorphicModel ):
	good = models.ForeignKey('Good') 
	status = models.ForeignKey('InventoryItemStatusType') 
	locatedAt = models.ForeignKey(Facility) 
	locatedWithin = models.ForeignKey('Container') 
	lot = models.ForeignKey('Lot') 

class SerializedInventoryItem( InventoryItem):
	serialNumber = models.CharField(max_length=250)

class NonSerializedInventoryItem( InventoryItem):
	quantityOnHand = models.IntegerField()

class InventoryItemVariance( models.Model):
	physicalInventoryDate = models.DateField()
	quantity = models.IntegerField();
	comment = models.CharField(max_length=250)
	reason = models.ForeignKey('Reason') 
	adjustmentFor = models.ForeignKey('InventoryItem') 

class Reason( models.Model):
	description = models.CharField(max_length=250)

class Container( models.Model):
	description = models.CharField(max_length=250)
	locatedAt = models.ForeignKey(Facility) 
	kind = models.ForeignKey('ContainerType') 
	
class ContainerType( models.Model):
	description = models.CharField(max_length=250)

class Lot( models.Model):
	description = models.CharField(max_length=250)
	quantity = models.IntegerField()
	creationDate = models.DateField(default = datetime.today())
	expirationDate = models.DateField(blank=True, null=True)

class InventoryItemStatusType( models.Model):
	description = models.CharField(max_length=250)

class ReorderGuideline( models.Model):
	guidelineFor = models.ForeignKey('Good')
	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank=True, null=True)
	reorderQuantity = models.IntegerField()
	reorderLevel = models.IntegerField()
	boundary = models.ForeignKey(GeographicBoundary)
	facility = models.ForeignKey(Facility)
	internalOrganization = models.ForeignKey(PartyRole, limit_choices_to={'partyRoleType__description':'Internal Organization'})
	

class SupplierProduct( models.Model):
	availableFrom = models.DateField(default = datetime.today())
	availableThru = models.DateField(blank=True, null=True)
	standardLeadTimeInDays = models.IntegerField(blank=True, null=True)
	product = models.ForeignKey('Product')
	organization = models.ForeignKey(Organization)
	preference = models.ForeignKey('PreferenceType')
	rating = models.ForeignKey('RatingType')
	def __unicode__(self):
		return self.Organization.name

class PreferenceType( models.Model):
	description = models.CharField(max_length=250)

class RatingType( models.Model):
	description = models.CharField(max_length=250)

class Identification( models.Model ):
	value = models.CharField(max_length=250)
	good = models.ForeignKey(Good)
	kind = models.ForeignKey('IdentificationType')
	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

class Category( models.Model ):
	product = models.ForeignKey(Product)
	categoryType = models.ForeignKey('CategoryType')
	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.categoryType.description

class Feature( PolymorphicModel ):
	description = models.CharField(max_length=250)
	category = models.ForeignKey('FeatureCategory')
	product = models.ManyToManyField('Product', through='FeatureApplicability')
	def __unicode__(self):
		return self.description

class Dimension( Feature ) :
	numberSpecified =models.IntegerField()
	measuredUsing = models.ForeignKey('UnitOfMeasure')
	def __unicode__(self):
		return '{0} {1}'.format( self.numberSpecified, self.measuredUsing.abbreviation)

class UnitOfMeasure( PolymorphicModel):
	abbreviation = models.CharField(max_length=15)
	description = models.CharField(max_length=100)
	def __unicode__(self):
		return self.abbreviation 

class TimeFrequencyMeasure( UnitOfMeasure):
	''' another measure '''

class CurrencyMeasure( UnitOfMeasure):
	''' Currencies '''

class UnitOfMeasureConversion( models.Model):
	convertFrom = models.ForeignKey('UnitOfMeasure', related_name='convertFrom_set')
	convertTo = models.ForeignKey('UnitOfMeasure', related_name='convertInto_set')
	conversionFactor = models.DecimalField( max_digits=5, decimal_places=3)
	def __unicode__(self):
		return '{0} * {1} = {2}'.format( self.convertFrom.abbreviation, self.conversionFactor, self.convertTo.abbreviation)

class FeatureApplicability( models.Model) :
	ApplicabilityChoices = (
		('Required' , 'Required'),
		('Standard' , 'Standard'),
		('Optional' , 'Optional'),
		('Selectable' , 'Selectable')
		)
	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank = True, null = True)
	product = models.ForeignKey('Product')
	feature = models.ForeignKey('Feature' )
	kind = models.CharField(max_length=10, choices=ApplicabilityChoices)
	def __unicode__(self):
		return self.feature.description

class FeatureInteraction( models.Model ):
	incompatibility = models.BooleanField()
	interactionDependancy = models.BooleanField()
	of = models.ForeignKey('Feature', related_name='of_set')
	factorIn = models.ForeignKey('Feature', related_name='factorIn_set')
	contextOf = models.ForeignKey('Product')

class CategoryType(models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	ofInterestTo = models.ManyToManyField( PartyType, through='MarketInterest')
	def __unicode__(self):
		return self.description

class MarketInterest( models.Model ):
	partyType = models.ForeignKey(PartyType)
	categoryType = models.ForeignKey(CategoryType)
	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

class IdentificationType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class FeatureCategory( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
