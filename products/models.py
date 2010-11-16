from django.db import models
from party.models import PartyType

class Product(models.Model):
	name = models.CharField(max_length=128)
	introductionDate = models.DateField(blank=True, null=True)
	salesDiscontinuationDate = models.DateField(blank=True, null=True)
	supportDiscontinuationDate = models.DateField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	categories = models.ManyToManyField( 'ProductCategoryType', through='ProductCategory')
	def __unicode__(self):
		return self.name

class Good(Product):
	identifiers = models.ManyToManyField( 'IdentificationType', through='Identification')
	def __unicode__(self):
		return self.name

class Service(Product):
	def __unicode__(self):
		return self.name
	
class ProductCategory( models.Model ):
	product = models.ForeignKey(Product)
	categoryType = models.ForeignKey('ProductCategoryType')
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

class ProductCategoryType(models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	ofInterestTo = models.ManyToManyField( PartyType, through='MarketInterest')
	def __unicode__(self):
		return self.description

class MarketInterest( models.Model ):
	partyType = models.ForeignKey(PartyType)
	categoryType = models.ForeignKey(ProductCategoryType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

class IdentificationType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class Identification( models.Model ):
	value = models.CharField(max_length=250)
	good = models.ForeignKey(Good)
	kind = models.ForeignKey('IdentificationType')
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

