from django.db import models
from Party import Party

class ContactMechanism(models.Model):
	comment = models.TextField( blank = True, null = True)

	class Meta:
		app_label = 'party'

class PartyContactMechanism(models.Model):
	party = models.ForeignKey(Party)
	contactMechanism = models.ForeignKey(ContactMechanism)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	acceptsSolicitations = models.BooleanField()
	class Meta:
		app_label = 'party'

