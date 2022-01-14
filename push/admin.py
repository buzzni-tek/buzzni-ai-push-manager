from django.contrib import admin
from push.models import PushCategory, PushMessage


class PushCategoryAdmin(admin.ModelAdmin):
    pass


class PushMessageAdmin(admin.ModelAdmin):
    pass


class ExtractUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(PushCategory, PushCategoryAdmin)
admin.site.register(PushMessage, PushMessageAdmin)
