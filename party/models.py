from django.db import models

class Party(models.Model):
	def __unicode__(self):
		return self.id

class Person( Party):
	firstName=models.CharField(max_length=128)
	middleName = models.CharField(max_length=128)
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
	def __unicode__(self):
		return self.description

class PartyClassification(models.Model):
	party = models.ForeignKey(Party)
	partyType = models.ForeignKey(PartyType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)

class RoleType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class PartyRoleType( RoleType):
	descriptionFor = models.ManyToManyField( Party, through='PartyRole')

class PartyRole(models.Model):
	party = models.ForeignKey(Party)
	partyRoleType = models.ForeignKey(PartyRoleType)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	
