from party.models import Person, Organization, PartyClassification, PartyType, PartyRoleType, PartyRole
from django.contrib import admin


class PartyClassificationInline(admin.TabularInline):
	model=PartyClassification
	extra=1

class PartyRoleInLine(admin.TabularInline):
	model=PartyRole
	extra=1

class PartyRoleTypeInLine(admin.TabularInline):
	model=PartyRoleType
	extra=1

class PartyTypeInLine(admin.TabularInline):
	model=PartyType
	extra=1

class PartyAdmin(admin.ModelAdmin):
	inlines=[PartyClassificationInline, PartyRoleInLine]

class PartyRoleTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRoleTypeInLine]

class PartyTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyTypeInLine]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType, PartyTypeAdmin)
admin.site.register(PartyRoleType, PartyRoleTypeAdmin)
