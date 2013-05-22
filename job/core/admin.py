from django.contrib import admin
from models import Company,Candidate,JobsCategory,Vacancy

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'size', 'about', )

admin.site.register(Company, CompanyAdmin)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','email','experience', 'education','location','looking_for', 'more_info')

admin.site.register(Candidate, CandidateAdmin)

class JobsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(JobsCategory, JobsCategoryAdmin)

class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title','sex','experience', 'education','location', 'jobs_category')

admin.site.register(Vacancy, VacancyAdmin)
