from django.db import models

# Create your models here.

class Student(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    matric = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.email

class Hostel(models.Model):
    hostelName = models.CharField(max_length=100)
    hostelType = models.CharField(max_length=100)
    hostelNumberRooms = models.IntegerField()
    hostelLevel = models.CharField(max_length=100)

    def __str__(self):
        return self.hostelName


class Room(models.Model):
    roomNumber = models.IntegerField()
    studentPerRoom = models.IntegerField()
    studentActualNumber = models.IntegerField()
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, default= None)
    
    def __str__(self):
        return str(self.roomNumber)
        


