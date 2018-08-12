from django.contrib import admin
from . models import language,subtopic,question,topic
# Register your models here.
admin.site.register(language)
admin.site.register(topic)
admin.site.register(subtopic)
admin.site.register(question)