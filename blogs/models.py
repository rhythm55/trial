from django.db import models

class blog(models.Model):
    language = models.CharField(max_length=50)
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
