from django.contrib import admin

from .models import language,topic,subtopic,sstopic

admin.site.register(language)
admin.site.register(topic)
admin.site.register(subtopic)
admin.site.register(sstopic)
