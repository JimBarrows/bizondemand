from party.models import Person, Organization, PartyClassification, PartyType
from django.contrib import admin


class PartyClassificationInline(admin.StackedInline):
	model=PartyClassification
	extra=3

class PartyAdmin(admin.ModelAdmin):
	fieldsets=[
	]
	inlines=[PartyClassificationInline]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType)
