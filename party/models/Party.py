from django.db import models

class Party(models.Model):
	def __unicode__(self):
		return 'Party'

	class Meta:
		app_label = 'party'

class Person( Party):
	firstName=models.CharField(max_length=128)
	middleName = models.CharField(max_length=128, blank=True, null = True)
	lastName = models.CharField(max_length=128)
	def __unicode__(self):
		return self.firstName + ' ' + self.middleName + ' '+ self.lastName
	class Meta:
		app_label = 'party'

class Organization( Party):
	name=models.CharField(max_length=128)
	def __unicode__(self):
		return self.name
	class Meta:
		app_label = 'party'

class PartyType(models.Model):
	description = models.CharField(max_length=250)
	descriptionFor = models.ManyToManyField( Party, through='PartyClassification')
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class PartyClassification(models.Model):
	party = models.ForeignKey(Party)
	partyType = models.ForeignKey(PartyType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyType.description
	class Meta:
		app_label = 'party'

class PartyRoleType( models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	descriptionFor = models.ManyToManyField( Party, through='PartyRole')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class PartyRole(models.Model):
	party = models.ForeignKey(Party)
	partyRoleType = models.ForeignKey(PartyRoleType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.partyRoleType.description
	class Meta:
		app_label = 'party'

class PartyRelationshipType(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=250, blank = True, null = True)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	fromRoleType = models.ForeignKey(PartyRoleType, related_name='from_role_type_set')
	toRoleType = models.ForeignKey(PartyRoleType, related_name='to_role_type_set')
	def __unicode__(self):
		return self.name
	class Meta:
		app_label = 'party'

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
	class Meta:
		app_label = 'party'

class PartyPostalAddress(models.Model):
	party = models.ForeignKey(Party)
	comment = models.TextField()
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	location = models.ForeignKey('PostalAddress')
	def __unicode__(self):
		return self.location.street1
	class Meta:
		app_label = 'party'

class PriorityType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class StatusType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'
	class Meta:
		app_label = 'party'
