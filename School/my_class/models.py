from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100,null=False)


    def __str__(self):
        return self.name
    


class Students_here(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    roll = models.IntegerField(null=False)


    def __str__(self):
        return "%s %s %s"%(self.first_name, self.last_name, self.roll)