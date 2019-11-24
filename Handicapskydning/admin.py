from django.contrib import admin
from Handicapskydning import models

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'date')


class ActivityAdmin(admin.ModelAdmin):
    fields = ('region', 'city', 'rank', 'date')


class ResultsAdmin(admin.ModelAdmin):
    fields = ('competition', 'file')


class DepartmentAdmin(admin.ModelAdmin):
    field = 'name'


class StaffMemberAdmin(admin.ModelAdmin):
    fields = ('profile_image', 'department', 'name', 'email', 'phone', 'address', 'city', 'postal_code', 'title')


class ClubAdmin(admin.ModelAdmin):
    fields = ('name', 'city', 'link')


class DokumentsAdmin(admin.ModelAdmin):
    fields = ('name', 'file')


class LaneAdmin(admin.ModelAdmin):
    field = 'picture'


class LinkAdmin(admin.ModelAdmin):
    fields = ('name', 'picture', 'link')


class CPictureAdmin(admin.StackedInline):
    model = models.CPictures
    max_num = 20
    min_num = 0


class CollectionsAdmin(admin.ModelAdmin):
    fields = ('name', 'year')
    inlines = [CPictureAdmin]


admin.site.register(models.Collections, CollectionsAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Lane, LaneAdmin)
admin.site.register(models.Documents, DokumentsAdmin)
admin.site.register(models.Club, ClubAdmin)
admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.StaffMember, StaffMemberAdmin)
admin.site.register(models.Results, ResultsAdmin)
admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.News, NewsAdmin)
