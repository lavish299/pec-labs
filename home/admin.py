from django.contrib import admin
from .models import Equipment,Secondary_Image

# Register your models here.

admin.site.site_header="PEC Equipment Rental"
admin.site.site_title="PEC Equipment Rental"

class Secondary_ImageAdmin(admin.StackedInline):
    model = Secondary_Image
    verbose_name_plural = 'More Images'
    verbose_name = 'Secondary Image'



@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each equipment.",
            'fields': (('equipment_name','primary_desc'),'rental','primary_img')
        }),
        ('Additional Information', {
            'description': "These fields are optional.",
            'fields': ('secondary_desc',),
            'classes': ('wide', 'extrapretty'),

        }),
    )
    inlines = [Secondary_ImageAdmin]



# admin.site.register(Equipment)
