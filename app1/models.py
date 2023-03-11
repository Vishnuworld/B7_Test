from statistics import mode
from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

# model

class ActiveP(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=0)


class CommanClass(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pk} -- {self.name}"

class Employee(CommanClass):
    salary = models.IntegerField()

class Persons(CommanClass):
    Address = models.CharField(max_length=100)
    City  = models.CharField(max_length=100)
    Age = models.IntegerField()
    is_delete = models.SmallIntegerField(default=0)
    active_persons = ActiveP()  # active_person
    objects = models.Manager()

    class Meta:
        db_table = "persons"


    def get_person_details(self):
        print(f"""--------Person ID:- {self.id}--------
Name:- {self.name}
Age:- {self.Age}
Address:- {self.Address}
City:- {self.City}
        """)

    @classmethod
    def get_active_persons(cls):
        return cls.objects.filter(is_delete=0)

    @classmethod
    def get_inactive_persons(cls):
        return cls.objects.filter(is_delete=1)

    @classmethod
    def get_avg_age(cls):
        all = Persons.objects.filter(is_delete=0).values_list("Age")
        lst = list(map(lambda x: x[0], all))
        avg = sum(lst)/len(lst)
        return avg


# assgnm -- 5
# class --- model -- 
# 6 methods --  
# db_shell.py -- abhi tak jo hamne orm queries -- ek orm query -- 2-2 example -- 
# sare commands -- runserver, 
# inactive persons -- model manager 
# carmodel example -- m2m -- 

# ERD

class College(CommanClass):
    address = models.CharField(max_length=100)
    est_date = models.DateField()

    class Meta:
        db_table = "college"
    
class Princi(CommanClass):
    exp = models.FloatField()
    salary = models.IntegerField()
    college = models.OneToOneField(College, on_delete=models.CASCADE)       # college_id

    class Meta:
        db_table = "princi"

class Department(CommanClass):
    staff_num = models.IntegerField()
    college = models.ForeignKey("College", on_delete=models.CASCADE, related_name="depts")

    class Meta:
        db_table = "dept"

class Students(CommanClass):
    age = models.IntegerField()
    marks = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="studs", null=True)
    class Meta:
        db_table = "student"

class Subjects(CommanClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Students)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, related_name="subjs", null=True)
    class Meta:
        db_table = "subject"

class Author(models.Model):
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    # publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name