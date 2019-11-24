from django.contrib import admin

from .models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Company.objects.all().count()
        if count == 0:
            return True
        return False


admin.site.register(Company, CompanyAdmin)
