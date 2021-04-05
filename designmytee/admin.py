from django.contrib import admin
from designmytee.models import Designer, Submission, Competition, Support_Request, ItemVideo
from embed_video.admin import AdminVideoMixin

# Register your models here.

#class UserAdmin(admin.ModelAdmin):
#    list_display = ('get_username')

#    def get_username(self, obj):
#        return obj.user.username

class DesignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'participations')
    prepopulated_fields = {'slug':('user',)}

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('competition', 'participant', 'id', 'submissionDescription', 'votes')
    
class CompetitionAdmin(admin.ModelAdmin):

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')
    prepopulated_fields = {'slug':('title',)}

    list_display = ('title', 'id', 'startDate', 'endDate', 'expiryDate')

    
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'contactNumber', 'contactEmail', 'suggestionsOrFeedback')
    
class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Designer, DesignerAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Support_Request, FeedbackAdmin)
admin.site.register(ItemVideo, VideoAdmin)