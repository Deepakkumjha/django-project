from django.contrib import admin
from contactus.models import Contact
# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display2=('email')
admin.site.register(Contact,contactAdmin)