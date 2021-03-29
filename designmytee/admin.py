from django.contrib import admin
from designmytee.models import Designer, Host, Submission, Competition, Support_Request

# Register your models here.

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'userID')
    
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'userID')
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('participant','submissionDescription', 'votes')
    
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'competitionID', 'startDate', 'endDate')
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'supportID', 'contactNumber', 'contactEmail', 'suggestionsOrFeedback')

admin.site.register(Designer, DesignerAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Support_Request, FeedbackAdmin)