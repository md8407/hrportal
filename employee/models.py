# from datetime import datetime
# from email import charset
# from os import terminal_size
# from django.db import models
# from django.forms import CharField, DateField, DateTimeField, EmailField, ImageField, TimeField
# # from matplotlib import image

# Create your models here.
# employee module
# class Employee(models.Model):
#     emp_name = models.CharField(max_length=50),
#     emp_mail = models.CharField(max_length=50),
#     emp_phone = models.CharField(max_length=50),
#     emp_gender = models.CharField(max_length=50),
#     emp_dob = models.CharField(max_length=50),
#     emp_add = models.CharField(max_length=50),
#     emp_type = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE),
#     emp_document = models.CharField(max_length=50),
#     emp_salary = models.IntegerField(),
#     emp_pic = ImageField,
#     emp_city = models.CharField(max_length=50),
#     emp_doj = models.CharField(max_length=50),


#     class Meta():
#         db_table = 'Employee_Info'


# #hr module
# class Hr(models.Model):
#     hr_name = models.CharField(max_length=50),
#     hr_phone = models.IntegerField(),
#     hr_email = models.CharField(max_length=50),
#     hr_pic = ImageField,

#     class Meta():
#         db_table = 'Hr_Info'


# #holiday module

# class Holiday(models.Model):
#     holiday_date = models.DateField(_(""), auto_now=False, auto_now_add=False),
#     holyday_name = models.CharField(_(""), max_length=50),

#     class Meta(models.Model):
#         db_table = 'Holiday_info'

# #Attendance
# class Attendance(models.Model):
#     atd_id = models.IntegerField(),
#     emp_id = models.IntegerField(),
#     atd_date = models.DateField(_(""), auto_now=False, auto_now_add=False),
#     atd_time =models.TimeField(_(""), auto_now=False, auto_now_add=False)

#     class Meta(models.Model):
#         db_table = 'Attendance_Info'

# #leaves module
# class Leaves(models.Model):
#     lev_id = models.IntegerField(),
#     lev_date = models.DateField(_(""), auto_now=False,auto_now_add=False),
#     lev_duration = models.IntegerField(),
#     lev_time = models.TimeField(_(""), auto_now=False, auto_now_add=False),
#     lev_reason = models.CharField(_(""), max_length=50),
#     emp_id = models.IntegerField(_("")),
#     atd_id = models.IntegerField(_("")),
#     dep_id = models.IntegerField(_("")),

#     class Meta(models.Model):
#         db_table = 'leaves_Info'


# #Salary module
# class Salary(models.Model):
#     sal_id = models.IntegerField(_("")),
#     emp_id = models.IntegerField(_("")),
#     dep_id = models.IntegerField(_("")),
#     salary = models.IntegerField(_("")),
#     sal_pf = models.IntegerField(),
#     sal_tax = models.IntegerField(),
#     atd_id = models.CharField(),

#     class Meta():
#         db_table ='Salary_info'

# #Team_leader
# class Team_Leader(models.Model):
#     team_id = models.IntegerField(),
#     team_name = models.CharField(_(""), max_length=50) 
#     team__member = models.CharField(_(""), max_length=50),
#     terminal_size = models.IntegerField(_("")),

#     class Meta():
#         db_table = 'team_leader_info'



