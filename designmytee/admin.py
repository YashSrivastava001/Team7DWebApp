from django.contrib import admin
from designmytee.models import Designer, Host, Submission, Competition

# Register your models here.

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'userID')
    
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'userID')
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('participant', 'votes')
    
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('competitionID', 'startDate', 'endDate')

admin.site.register(Designer, DesignerAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)