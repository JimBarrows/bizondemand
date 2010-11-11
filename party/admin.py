from party.models import *
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

class CommunicationEventInLine(admin.TabularInline):
	model=CommunicationEvent
	extra=1

class PartyRelationshipTypeInLine(admin.TabularInline):
	model=PartyRelationshipType
	extra=1

class ContainsGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='contains'
	extra=1

class ContainedByGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='containedBy'

class ContainedByGeographicBoundaryAssociationInLine(admin.TabularInline):
	model=GeographicBoundaryAssociation
	fk_name='containedBy'

class SpecifiedForPostalAddressBoundaryInLine(admin.TabularInline):
	model=PostalAddressBoundary
	fk_name='specifiedFor'

class InBoundaryPostalAddressBoundaryInLine(admin.TabularInline):
	model=PostalAddressBoundary
	fk_name='inBoundary'

class PartyPostalAddressInLine(admin.TabularInline):
	model=PartyPostalAddress
	extra=1

class PartyAdmin(admin.ModelAdmin):
	inlines=[PartyClassificationInline, PartyRoleInLine, PartyPostalAddressInLine ]

class PartyRoleTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRoleTypeInLine]

class PartyTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyTypeInLine]

class PartyRelationshipTypeAdmin(admin.ModelAdmin):
	inlines=[ PartyRelationshipTypeInLine]

class PartyRelationshipAdmin(admin.ModelAdmin):
	inlines=[ CommunicationEventInLine]

class GeographicBoundaryAdmin(admin.ModelAdmin):
	inlines=[ ContainsGeographicBoundaryAssociationInLine, 
		ContainedByGeographicBoundaryAssociationInLine
	]

class PostalAddressAdmin(admin.ModelAdmin):
	inlines=[ SpecifiedForPostalAddressBoundaryInLine
	]

class PartyRelationshipAdmin(admin.ModelAdmin):
	inlines=[ CommunicationEventInLine]

admin.site.register(Person, PartyAdmin)
admin.site.register(Organization, PartyAdmin)
admin.site.register(PartyType, PartyTypeAdmin)
admin.site.register(PartyRoleType, PartyRoleTypeAdmin)
admin.site.register(PartyRelationshipType, PartyRelationshipTypeAdmin)
admin.site.register(PartyRelationship, PartyRelationshipAdmin )
admin.site.register(PriorityType )
admin.site.register(StatusType )
admin.site.register(GeographicBoundaryType )
admin.site.register(GeographicBoundary, GeographicBoundaryAdmin )
admin.site.register(GeographicBoundaryAssociation)
admin.site.register(PostalAddress, PostalAddressAdmin)
admin.site.register(PostalAddressBoundary)
