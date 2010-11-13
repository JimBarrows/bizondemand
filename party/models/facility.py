from django.db import models
from Party import Party
from ContactMechanism import ContactMechanism

class FacilityType( models.Model):
	description = models.CharField(max_length=250)
	kindOf = models.ForeignKey('self', blank = True, null = True, related_name='subType')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class FacilityRoleType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class Facility( models.Model):
	description = models.CharField(max_length=250)
	squareFootage = models.IntegerField( blank=True, null = True)
	facilityType = models.ForeignKey(FacilityType)
	partOf = models.ForeignKey('self', blank = True, null = True, related_name='madeUpOf')
	roles = models.ManyToManyField( FacilityRoleType, through='FacilityRole')
	contactMechanisms = models.ManyToManyField( ContactMechanism, through='FacilityContactMechanism')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class FacilityContactMechanism(models.Model):
	facility = models.ForeignKey(Facility)
	contactMechanism = models.ForeignKey(ContactMechanism)
	comment = models.TextField(blank=True, null=True)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	acceptsSolicitations = models.BooleanField()
	class Meta:
		app_label = 'party'


class FacilityRole( models.Model):
	party = models.ForeignKey(Party, blank=True, null=True)
	facility = models.ForeignKey(Facility)
	roleType = models.ForeignKey(FacilityRoleType)
	fromDate = models.DateField()
	thruDate = models.DateField( blank=True, null=True)
	class Meta:
		app_label = 'party'

