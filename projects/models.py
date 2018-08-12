from django.db import models

class project(models.Model):
    language = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    overlay_dis = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.project_name

class steps(models.Model):
    project = models.ForeignKey('project',on_delete=models.CASCADE)
    step_no = models.IntegerField()
    step_dis = models.CharField(max_length=800)
    video_link = models.TextField(max_length=50)

    def __str__(self):
        return str(self.step_no)


