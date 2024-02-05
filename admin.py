from django.contrib import admin
from .models import Profile, Univer_Profile
"""Club_Profile, Open_Position_for_Un, Open_Position_for_Cl, Extra_Languages, \
    Achivment, Teem"""


class Profel_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Univer_Profile_id(admin.ModelAdmin):
    readonly_fields = ('id','counter_start','count_pos','telegram_id',)

'''
class Club_Profile_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Open_Position_for_Un_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Open_Position_for_Cl_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Extra_Languages_id(admin.ModelAdmin):
    readonly_fields = ('id',)


class Achivment_id(admin.ModelAdmin):
    readonly_fields = ('id',)

class Teem_id(admin.ModelAdmin):
    readonly_fields = ('id',)

'''
admin.site.register(Profile, Profel_id)

admin.site.register(Univer_Profile, Univer_Profile_id)
'''
admin.site.register(Club_Profile, Club_Profile_id)

admin.site.register(Open_Position_for_Un, Open_Position_for_Un_id)

admin.site.register(Open_Position_for_Cl, Open_Position_for_Cl_id)

admin.site.register(Extra_Languages, Extra_Languages_id)

admin.site.register(Achivment, Achivment_id)

admin.site.register(Teem, Teem_id)
'''