from django.db import models
from Party import Party, PartyRole, PartyRelationship
from ContactMechanism import ContactMechanism

class CommunicationEvent( models.Model):
	dateTimeStarted = models.DateTimeField()
	dateTimeEnded = models.DateTimeField()
	note = models.TextField()
	kind = models.ForeignKey('CommunicationEventType')
	status = models.ForeignKey('CommunicationEventStatusType')
	occursVia = models.ForeignKey(ContactMechanism)
	context = models.ForeignKey(PartyRelationship)
	kase = models.ForeignKey('Kase')
	involving = models.ManyToManyField( 'CommunicationEventRoleType', through='CommunicationEventRole')
	categorizedBy = models.ManyToManyField( 'CommunicationEventPurposeType', through='CommunicationEventPurpose')
	def __unicode__(self):
		return self.note
	class Meta:
		app_label = 'party'

class Kase( models.Model):
	dateTimeStarted = models.DateTimeField()
	name = models.CharField(max_length=250)
	description = models.TextField()
	involving = models.ManyToManyField( 'KaseRoleType', through='KaseRole')
	class Meta:
		app_label = 'party'

class CommunicationEventType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class CommunicationEventStatusType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'


class CommunicationEventRole( models.Model):
	kind = models.ForeignKey('CommunicationEventRoleType')
	event = models.ForeignKey(CommunicationEvent)
	forA = models.ForeignKey(Party)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	class Meta:
		app_label = 'party'

class CommunicationEventRoleType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class CommunicationEventPurpose( models.Model):
	kind = models.ForeignKey('CommunicationEventPurposeType')
	event = models.ForeignKey(CommunicationEvent)
	forA = models.ForeignKey(Party)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	class Meta:
		app_label = 'party'

class CommunicationEventPurposeType( models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class KaseRoleType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class KaseRole( models.Model):
	kind = models.ForeignKey('KaseRoleType')
	kase = models.ForeignKey(Kase)
	forA = models.ForeignKey(Party)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	class Meta:
		app_label = 'party'
