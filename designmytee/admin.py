from django.contrib import admin
from designmytee.models import Designer, Submission, Competition, Support_Request

# Register your models here.

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'participations')
    
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('participant', 'id', 'submissionDescription', 'votes')
    
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'startDate', 'endDate')
    prepopulated_fields = {'slug':('title',)}
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'contactNumber', 'contactEmail', 'suggestionsOrFeedback')

admin.site.register(Designer, DesignerAdmin)
#admin.site.register(Host, HostAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Support_Request, FeedbackAdmin)