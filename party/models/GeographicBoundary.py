from django.db import models
from party import *

class GeographicBoundaryType(models.Model):
	description = models.CharField(max_length=250, blank = True, null = True)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class GeographicBoundary(models.Model):
	name = models.CharField(max_length=250, blank = True, null = True)
	abbrev = models.CharField(max_length=10, blank = True, null = True)
	geocode = models.CharField(max_length=250, blank = True, null = True)
	geographicBoundaryType = models.ForeignKey(GeographicBoundaryType)
	def __unicode__(self):
		return self.name
	class Meta:
		app_label = 'party'

class GeographicBoundaryAssociation(models.Model):
	contains = models.ForeignKey(GeographicBoundary, related_name='contains_set')
	containedBy = models.ForeignKey(GeographicBoundary, related_name='containedBy_set')
	def __unicode__(self):
		return self.containedBy.name + " - " + self.contains.name 
	class Meta:
		app_label = 'party'

