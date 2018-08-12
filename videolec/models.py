from django.db import models

class video(models.Model):
    language = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    sub_topic = models.CharField(max_length=200)
    url = models.TextField()
    theory = models.TextField()
