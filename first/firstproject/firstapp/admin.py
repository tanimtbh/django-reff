from django.contrib import admin
from firstapp.models import Topic, Webpage, AccessRecord
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)