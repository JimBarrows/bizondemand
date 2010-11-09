from party.models import Person, Organization, PartyClassification, PartyType, PartyRoleType, PartyRole
from django.contrib import admin


class PartyClassificationInline(admin.StackedInline):
	model=PartyClassification
	extra=3

class PartyRoleInLine(admin.StackedInline):
	model=PartyRole
	extra=3

class PartyAdmin(admin.ModelAdmin):
	fieldsets=[
	]
	inlines=[PartyClassificationInline, PartyRoleInLine]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType)
admin.site.register(PartyRoleType)
