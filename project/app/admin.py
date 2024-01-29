from django.contrib import admin
from .models import Parce, Dizajner


class ParceInline(admin.StackedInline):
    model = Parce
    extra = 1


class DizajnAdmin(admin.ModelAdmin):
    inlines = [ParceInline]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class ParceAdmin(admin.ModelAdmin):
    exclude = ("user", )

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user):
            return True
        return False


admin.site.register(Parce)
admin.site.register(Dizajner)

# Register your models here.
