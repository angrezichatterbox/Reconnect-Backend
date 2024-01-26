from django.contrib import admin

from .models import EventPage, RaiseHand, RequestInstitute, InstituteDetails, EditProfile
admin.site.register(EventPage)
admin.site.register(RequestInstitute)
admin.site.register(InstituteDetails)
admin.site.register(EditProfile)

