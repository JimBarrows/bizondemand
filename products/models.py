from django.db import models
from polymorphic import PolymorphicModel
from party.models import PartyType
from datetime import datetime
from party.models import Organization, Facility, PartyRole, GeographicBoundary

class Product(PolymorphicModel):
	name = models.CharField(max_length=128)
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

class UnitOfMeasure( models.Model):
	abbreviation = models.CharField(max_length=15)
	description = models.CharField(max_length=100)
	def __unicode__(self):
		return self.abbreviation 

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
