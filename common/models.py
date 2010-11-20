from django.db import models
from datetime import datetime


# Create your models here.

class DateRange(models.Model) :

	fromDate = models.DateField(default = datetime.today())
	thruDate = models.DateField(blank = True, null = True)

