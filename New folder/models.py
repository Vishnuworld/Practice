from django.db import models

# Create your models here.

class Student(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   address = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "student_info"


s1 = Student(name='A',mail='gmail1',address='Pune1',phonenumber=1234)
s2 = Student(name='B',mail='gmail2',address='Pune2',phonenumber=5678)
s3 = Student(name='C',mail='gmail3',address='Pune3',phonenumber=1111)
s4 = Student(name='D',mail='gmail4',address='Pune4',phonenumber=2222)
s5 = Student(name='E',mail='gmail5',address='Pune5',phonenumber=3333)

