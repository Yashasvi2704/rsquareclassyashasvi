from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# Rsquare User
class RsquareAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('role', 'branch')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'branch', 'phone_no')}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'branch', 'phone_no')}),
    )
    pass
admin.site.register(models.RsquareUser, RsquareAdmin)

# Branch
admin.site.register(models.Branch)

# Subject and Course
admin.site.register(models.SubjectGroup)
admin.site.register(models.Subject)
admin.site.register(models.Course)
admin.site.register(models.CourseSubject)
admin.site.register(models.Batch)
admin.site.register(models.AcademicYear)
admin.site.register(models.BatchSubjects)
