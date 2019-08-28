from django.db import models

class LeapYear(models.Model):
    year = models.IntegerField()
    is_leap = models.BooleanField(default=False)

    def __str__(self):
        return str(self.year)
