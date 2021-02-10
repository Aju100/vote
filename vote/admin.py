from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Voting"
admin.site.site_title = "Polling"
admin.site.index_title = "Welcome to Voting Admin Area"


admin.site.register(Question)
admin.site.register(Choice)