from django.db import models

class LeapYear(models.Model):
    year = models.IntegerField(max_length=4)
    is_leap = models.BooleanField(default=False)

    def __str__(self):
        return self.year
