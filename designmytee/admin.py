from django.contrib import admin
from designmytee.models import Designer, Submission, Competition, Support_Request, ItemVideo
from embed_video.admin import AdminVideoMixin

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('get_username')

#    def get_username(self, obj):
#        return obj.user.username

# Below admin classes are created to determine what aspects of the variouse models are shown in the django admin interface

# The designer admin shows the user/username, the designerID and the number of participations

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'participations')
    prepopulated_fields = {'slug':('user',)}
    
# The submission admin shows the competition name, the participant, the submissionID, the Submission description and the number of votes for the submission

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('competition', 'participant', 'id', 'submissionDescription', 'votes')
    
# The competiton Admin shows the competition title, the competiton ID, the start date, end date and expiry date for the competition   

class CompetitionAdmin(admin.ModelAdmin):

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')
    prepopulated_fields = {'slug':('title',)}

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')

# The Support Request admin shows the first and last name, the contact number and email and the feedback/ suggestion that was submitted  
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'contactNumber', 'contactEmail', 'suggestionsOrFeedback')
    
# The video admin simply shows the video object    
    
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

# registers variouse admins and models with the admin site

admin.site.register(Designer, DesignerAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Support_Request, FeedbackAdmin)
admin.site.register(ItemVideo, VideoAdmin)