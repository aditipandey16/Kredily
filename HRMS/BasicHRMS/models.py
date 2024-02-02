from django.db import models
import datetime

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    attendance_date = models.DateField(default=datetime.date.today)
    is_present = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        app_label = 'BasicHRMS'
        