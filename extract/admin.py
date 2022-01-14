from django.contrib import admin
from extract.models import Extract, ExtractProduct, ExtarctUser


class ExtractAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
       super(ExtractAdmin, self).save_model(request, obj, form, change)


class ExtractProductAdmin(admin.ModelAdmin):
    pass


class ExtractUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Extract, ExtractAdmin)
admin.site.register(ExtractProduct, ExtractProductAdmin)
admin.site.register(ExtarctUser, ExtractUserAdmin)
