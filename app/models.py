from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Classhave(models.Model):
    classes=models.CharField(max_length=180)
    desc=models.CharField(max_length=360,null=True)
class Batch(models.Model):
    batch_title=models.CharField(max_length=180,null=True)
    batch_starting_time=models.TimeField(null=True)
    batch_ending_time=models.TimeField(null=True)
class Students(models.Model):
    first_name=models.CharField(max_length=180 ,null=True)
    last_name=models.CharField(max_length=180 ,null=True)
    email=models.CharField(max_length=180 ,null=True)
    dob=models.DateField ( null=True)
    father=models.CharField(max_length=180 ,null=True)
    mother=models.CharField(max_length=180 ,null=True)
    father_occupation=models.CharField(max_length=180 ,null=True)
    mother_occupation=models.CharField(max_length=180 ,null=True)
    password=models.CharField(max_length=180 ,null=True)
    joined_date=models.DateField(auto_now_add=True,null=True)
    batch=models.ForeignKey(Batch,max_length=180,null=True,on_delete=models.CASCADE)
    to_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    to_class=models.ForeignKey(Classhave,on_delete=models.CASCADE,null=True)
class Department(models.Model):
    name=models.CharField(max_length=180)

class Teacher(models.Model):
    first_name=models.CharField(max_length=180,null=True)
    last_name=models.CharField(max_length=180,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    dob=models.DateField(null=True)
    email=models.CharField(max_length=180,null=True)
    hse_board=models.CharField(max_length=180,null=True)
    hse_percent=models.IntegerField(null=True)
    degree=models.CharField(max_length=180,null=True)
    score=models.IntegerField(null=True)
    password=models.CharField(max_length=180,null=True)
    joined_date=models.DateField(auto_now_add=True,null=True)
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class Departandhead (models.Model):
    department=models.ForeignKey(Department,max_length=180,null=True,on_delete=models.CASCADE)
    headname=models.ForeignKey(Teacher,max_length=180,null=True,on_delete=models.CASCADE)
class To_msg(models.Model):
    content=models.CharField(max_length=400,null=True)
    to_student=models.BooleanField(null=True)
    to_teacher=models.BooleanField(null=True)
    to_admin=models.BooleanField(null=True)
    user_type=models.CharField(max_length=200,null=True)
    sent_by=models.CharField(max_length=400,null=True)
class Timetable(models.Model):
    classes=models.ForeignKey(Classhave,on_delete=models.CASCADE,null=True)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(Departandhead,on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=200,null=True)
    classlink=models.CharField(max_length=200,null=True)
