from django.contrib import admin

from . import models
# Register your models here.


class InvitationEmailAdmin(admin.ModelAdmin):
    exclude = ('to_email',)

    def save_model(self, request, obj, form, change):
        print('Save from admin called')
        super(InvitationEmailAdmin, self).save_model(request, obj, form, change)

admin.site.register(models.InvitationEmail, InvitationEmailAdmin)
