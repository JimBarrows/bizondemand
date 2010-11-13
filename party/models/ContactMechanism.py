from django.db import models
from Party import Party, PartyRoleType
from GeographicBoundary import GeographicBoundary

class ContactMechanismPurposeType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class ContactMechanism(models.Model):
	comment = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return 'Contact Mechanism'
	class Meta:
		app_label = 'party'

class PartyContactMechanism(models.Model):
	party = models.ForeignKey(Party)
	contactMechanism = models.ForeignKey(ContactMechanism)
	partyRoleType = models.ForeignKey(PartyRoleType, blank=True, null=True)
	purpose = models.ManyToManyField( ContactMechanismPurposeType, through='PartyContactMechanismPurpose')
	comment = models.TextField(blank=True, null=True)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	acceptsSolicitations = models.BooleanField()
	class Meta:
		app_label = 'party'

class PartyContactMechanismPurpose(models.Model):
	contactMechanism = models.ForeignKey(PartyContactMechanism)
	contactMechanismType = models.ForeignKey(ContactMechanismPurposeType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.contactMechanismType.description
	class Meta:
		app_label = 'party'

class PostalAddress(ContactMechanism):
	street1 = models.CharField(max_length=250, )
	street2 = models.CharField(max_length=250, blank = True, null = True)
	directions = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return self.street1
	class Meta:
		app_label = 'party'

class PostalAddressBoundary(models.Model):
	specifiedFor = models.ForeignKey(PostalAddress, related_name='specifiedFor')
	inBoundary = models.ForeignKey(GeographicBoundary, related_name='inBoundary')
	def __unicode__(self):
		return self.specifiedFor.street1 + " - " + self.inBoundary.name
	class Meta:
		app_label = 'party'
	

class EmailAddress( ContactMechanism):
	email = models.EmailField()
	def __unicode__(self):
		return self.email
	class Meta:
		app_label = 'party'

class IpAddress( ContactMechanism):
	ipAddress = models.IPAddressField()
	def __unicode__(self):
		return self.iPAddressField
	class Meta:
		app_label = 'party'

class UrlAddress( ContactMechanism):
	url = models.URLField()
	def __unicode__(self):
		return self.url
	class Meta:
		app_label = 'party'

class PhoneNumber( ContactMechanism):
	countryCode = models.CharField(max_length=7)
	areaCode = models.CharField(max_length=7)
	number = models.CharField(max_length=15)
	extension = models.CharField(max_length=15)
	def __unicode__(self):
		return '+{} ({}) {} {}'.format(countryCode, areaCode, number, extendsion)
	class Meta:
		app_label = 'party'
