from party.models import Person, Organization, PartyClassification, PartyType, PartyRoleType, PartyRole
from django.contrib import admin


class PartyClassificationInline(admin.StackedInline):
	model=PartyClassification
	extra=3

class PartyRoleInLine(admin.StackedInline):
	model=PartyRole
	extra=3

class PartyRoleTypeInLine(admin.TabularInline):
	model=PartyRoleType
	extra=1

class PartyAdmin(admin.ModelAdmin):
	inlines=[PartyClassificationInline, PartyRoleInLine]

class PartyRoleTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRoleTypeInLine]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType)
admin.site.register(PartyRoleType, PartyRoleTypeAdmin)
