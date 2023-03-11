

from audioop import avg
from cmath import pi
from email.headerregistry import Address
from unicodedata import name
from app1.models import *

# to fetch all data
# all_data = Persons.objects.all()

# to change
# p_obj = Persons.objects.get(City="Pune", Address="Wakad")  # and query
# print(p_obj.__dict__)
# p_obj.name = "pqr"
# p_obj.Address = "Kothrud"
# p_obj.Age = 25
# p_obj.save()

# if all_data.exists():
#     print("Data Present")


# for i in all_data:
#     print(i.__dict__)


# to see the corresponding sql query for django orm query -- 
# data = Modelname.objects.all()
# str(data.query)   -- sql query  

# >>> p2 = Persons(FirstName="xyz", Address="Wakad", City="Pune", Age=22)       
# >>> p2.save()

# Persons.objects.all()
# Persons.objects.get()  # gives single record,, if record is more than 2, it raises -- app1.models.Persons.MultipleObjectsReturned: get() returned more than one Persons -- it returned 2!

# Persons.objects.filter()

# > Persons.objects.filter(id__lte=2)  -- lt, gt, lte, gte
# > Persons.objects.filter(FirstName__contains="a")

# __startswith
# __endswith
# __contains
# __gt, lt, gte, lte
# __in 
# qs = Persons.objects.all().exclude(name="abc")
# print(str(qs.query))

# qs = Persons.objects.all().values_list("name") # 
# print(str(qs.query))
# print(qs)




# queryset = Persons.objects.filter(name__startswith='x') & Persons.objects.filter(Age__gt=21)
# print(str(queryset.query))
# from django.db.models import Q
# qs = Persons.objects.filter(Q(name__startswith='a')|Q(Age__gt=21))
# print(qs)
# print(str(qs.query))


# data = dict(list(Persons.objects.all().values_list("name", "Age")))

# data = Persons.objects.all().only("name")
# for i in data:
#     print(i)


# single_data = Persons.objects.get(id=1)
# print(single_data)


# CRUD
# create
# 1.
# p_obj = Persons(name="jkl", Address="Shivaji Nagar", City="Aurangabad", Age=29)
# obj = p_obj.save()  # returns None
# print(obj)

# 2.
# p_obj = Persons.objects.create(name="ghi", Address="Sai Nagar", City="Amrawati", Age=33)  # returns created object
# print(p_obj)

# Read
# all, 
# .get

# data = Persons.objects.filter(City="Pune")[0:2]
# print(data)

# update

# data = Persons.objects.all()
# for i in data:
    # i.get_person_details()
# data.Age = 24
# data.save()

# --- bulk update

# data = Persons.objects.filter(Age__in=[21, 24, 25])
# data.update(Age=22)
# print(data)


# bulk create? -- 

# delete



# p = Persons.objects.all().values_list("Age")
# reduce(lambda a, b: a[0]+b[0], p)

# print(Persons.get_avg_age())

# print(dir(Persons.objects))

# c = Persons.objects.count()

# c = Persons.objects.first()
# print(c)

# p = Persons.objects.filter(is_delete=0)
# print(p)

# data = Persons.get_active_persons()
# print(data)

# data = Persons.get_inactive_persons()
# print(data)

# print(Persons.active_persons.all())

# exec(open(r'G:\Class\B7\Code_Files\B7_Django\firstproject\db_shell.py').read())


# c1 = College.objects.get(id=1)
# print(dir(c1))
# depts = c1.depts.all()
# studs_list = []
# for i in depts:
    # studs_list.extend(list(i.studs.all()))
# print(studs_list)

# print(c1.est_date)
# all_dept = c1.depts.all()
# print(all_dept)



# d1 = Department.objects.get(id=3)
# print(d1.studs.all())



# print(c1.princi)

# print(p1.college)


# user_inp = int(input("Enter id:- "))
# try:
#     p1 = Princi.objects.get(id=user_inp)
#     print(p1)
# except Princi.DoesNotExist:
#     print(f"Princi does not exists for id {user_inp}")

# print("final")


# s1 = Students.objects.get(id=4)
# print(s1.subjects_set.all())

# print(dir(s1))
# print(s1.department.college.address)

# subj = Subjects.objects.get(id=4)
# print(subj.student.all()[0])
# data = subj.department
# print(data)


from django.utils import timezone

# c1 = College.objects.create(address="Amrawati", est_date=timezone.now())

# print(c1)


# clg = College.objects.get(id=3)

# Princi.objects.create(name="Princi3", exp=8, salary=80000, college=clg)
# Princi.objects.create(name="Princi3", exp=8, salary=80000, college_id=3)

# Department.objects.create(name="Instru", staff_num=6, college_id=3)
# Department.objects.create(name="Comp", staff_num=4, college_id=3)
# Department.objects.create(name="IT", staff_num=9, college_id=3)



# s1 = Students.objects.create(name="E", marks=45, age=18, department_id=1)

# s1 = Students.objects.first()

# d1 = Department.objects.get(id=1)
# print(dir(d1))
# d1.studs.add(studs[0], studs[1], studs[2], studs[3], studs[4])
# d1.studs.add(studs[1])
# d1.studs.add(studs[2])
# d1.studs.add(studs[3])
# d1.save()

# s1.department = d1
# s1.save()

# d1 = Department.objects.filter(college__name="DY Patil")
# print(d1)


# print(Students.objects.filter(department__college__name="Ram Meghe"))

print(Subjects.objects.filter(department__college__name="DY Patil"))