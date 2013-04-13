from django.contrib import admin
from models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'create_date')

admin.site.register(Company, CompanyAdmin)
