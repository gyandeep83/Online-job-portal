from django.contrib import admin
from .models import signup, IT_Companies, JobDescription, Feedback, JobApplication

admin.site.register(signup)
admin.site.register(IT_Companies)
admin.site.register(JobDescription)
admin.site.register(Feedback)
admin.site.register(JobApplication)

