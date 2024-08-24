from django.db import models
from admin_master.models import Subject,Class,Division,Department,Designation,Qualification,Employee_Category

class adminemp(models.Model):
    empcatid=models.ForeignKey(Employee_Category,on_delete=models.CASCADE)
    empname=models.CharField(max_length=100)
    dob=models.DateField()
    mobile=models.IntegerField(default=0)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    joindate=models.DateField()
    photo=models.ImageField(upload_to='employee_photos/',blank=True,null=True)
    qualifid=models.ForeignKey(Qualification,on_delete=models.CASCADE)
    desigid=models.ForeignKey(Designation,on_delete=models.CASCADE)
    dptid=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.PositiveIntegerField()
    barcode=models.ImageField(upload_to='barcode/',blank=True,null=True)
    GENDER_CHOICES = [
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    ]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    status=models.BooleanField(default=True)

class scd(models.Model):
    empid=models.ForeignKey(adminemp,on_delete=models.CASCADE)
    classid=models.ForeignKey(Class,on_delete=models.CASCADE)
    divid=models.ForeignKey(Division,on_delete=models.CASCADE)
    subid=models.ForeignKey(Subject,on_delete=models.CASCADE)


class empdesig(models.Model):
    empid=models.ForeignKey(adminemp,on_delete=models.CASCADE)
    desigid=models.ForeignKey(Designation,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)


class empdpt(models.Model):
    empid=models.ForeignKey(adminemp,on_delete=models.CASCADE)
    dptid=models.ForeignKey(Department,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)

class salary(models.Model):
    empid = models.ForeignKey(adminemp, on_delete=models.CASCADE, related_name='salaries')
    salary = models.PositiveIntegerField()
    from_date=models.DateField()
    to_date = models.DateTimeField(null=True, blank=True)
# Create your models here.
