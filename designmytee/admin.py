from django.contrib import admin
from designmytee.models import Designer, Submission, Competition, Support_Request

# Register your models here.

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'participations')
    
    
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('competition', 'participant', 'id', 'submissionDescription', 'votes')
    
class CompetitionAdmin(admin.ModelAdmin):

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')
    prepopulated_fields = {'slug':('title',)}

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')

    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'contactNumber', 'contactEmail', 'suggestionsOrFeedback')

admin.site.register(Designer, DesignerAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Support_Request, FeedbackAdmin)