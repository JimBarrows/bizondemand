from django.db import models

class Party(models.Model):
	def __unicode__(self):
		return self.id

class Person( Party):
	firstName=models.CharField(max_length=128)
	middleName = models.CharField(max_length=128, blank=True, null = True)
	lastName = models.CharField(max_length=128)
	def __unicode__(self):
		return self.firstName + ' ' + self.middleName + ' '+ self.lastName

class Organization( Party):
	name=models.CharField(max_length=128)
	def __unicode__(self):
		return self.name

class PartyType(models.Model):
	description = models.CharField(max_length=250)
	descriptionFor = models.ManyToManyField( Party, through='PartyClassification')
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	def __unicode__(self):
		return self.description

class PartyClassification(models.Model):
	party = models.ForeignKey(Party)
	partyType = models.ForeignKey(PartyType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description

class PartyRoleType( models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	descriptionFor = models.ManyToManyField( Party, through='PartyRole')
	def __unicode__(self):
		return self.description

class PartyRole(models.Model):
	party = models.ForeignKey(Party)
	partyRoleType = models.ForeignKey(PartyRoleType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyRoleType.description

class PartyRelationshipType(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=250, blank = True, null = True)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	fromRoleType = models.ForeignKey(PartyRoleType, related_name='from_role_type_set')
	toRoleType = models.ForeignKey(PartyRoleType, related_name='to_role_type_set')
	def __unicode__(self):
		return self.name

class PartyRelationship(models.Model):
	comment = models.TextField()
	relationshipType = models.ForeignKey(PartyRelationshipType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	fromRole = models.ForeignKey(PartyRole, related_name='from_role_set')
	toRole = models.ForeignKey(PartyRole, related_name='to_role_set')
	priority = models.ForeignKey('PriorityType', blank=True, null = True)
	status = models.ForeignKey('StatusType', blank=True, null = True)
	def __unicode__(self):
		return self.comment

class PartyPostalAddress(models.Model):
	party = models.ForeignKey(Party)
	comment = models.TextField()
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	location = models.ForeignKey('PostalAddress')
	def __unicode__(self):
		return self.location.street1

class CommunicationEvent(models.Model):
	started = models.DateTimeField()
	ended = models.DateTimeField()
	note = models.TextField()
	relationship = models.ForeignKey(PartyRelationship)
	def __unicode__(self):
		return self.note

class PriorityType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class StatusType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class GeographicBoundaryType(models.Model):
	description = models.CharField(max_length=250, blank = True, null = True)
	def __unicode__(self):
		return self.description

class GeographicBoundary(models.Model):
	name = models.CharField(max_length=250, blank = True, null = True)
	abbrev = models.CharField(max_length=10, blank = True, null = True)
	geocode = models.CharField(max_length=250, blank = True, null = True)
	geographicBoundaryType = models.ForeignKey(GeographicBoundaryType)
	def __unicode__(self):
		return self.name

class GeographicBoundaryAssociation(models.Model):
	contains = models.ForeignKey(GeographicBoundary, related_name='contains_set')
	containedBy = models.ForeignKey(GeographicBoundary, related_name='containedBy_set')
	def __unicode__(self):
		return self.containedBy.name + " - " + self.contains.name 

class PostalAddress(models.Model):
	street1 = models.CharField(max_length=250, )
	street2 = models.CharField(max_length=250, blank = True, null = True)
	directions = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return self.street1
	
class PostalAddressBoundary(models.Model):
	specifiedFor = models.ForeignKey(PostalAddress, related_name='specifiedFor')
	inBoundary = models.ForeignKey(GeographicBoundary, related_name='inBoundary')
	def __unicode__(self):
		return self.specifiedFor.street1 + " - " + self.inBoundary.name
	

