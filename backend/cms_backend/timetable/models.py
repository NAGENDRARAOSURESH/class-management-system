from django.db import models

class Timetable(models.Model):
    day = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.subject
