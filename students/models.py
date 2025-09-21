from django.db import models

class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()

    def total(self):
        return self.maths + self.physics + self.chemistry

    def percentage(self):
        return round(self.total() / 3, 2)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
