from django.db import models

# Create your models here.

class language(models.Model):
    language_name = models.CharField(max_length= 50)

    def __str__(self):
        return self.language_name

class topic(models.Model):
    language_name = models.ForeignKey('language',on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name

class subtopic(models.Model):
    topic_name = models.ForeignKey('topic',on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=100)
    subtopic_no = models.IntegerField()

    def __str__(self):
        return self.subtopic_name

class sstopic(models.Model):
    subtopic_name = models.ForeignKey('subtopic',on_delete=models.CASCADE)
    sstopic_name = models.CharField(max_length=100)
    material = models.TextField(max_length=1000)
    sstopic_no = models.IntegerField()

    def __str__(self):
        return self.sstopic_name