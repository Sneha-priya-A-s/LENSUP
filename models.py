from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class Photographer(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    photo=models.CharField(max_length=400)
    dob=models.DateField()
    experiance=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Category(models.Model):
    name=models.CharField(max_length=30)

class Contents(models.Model):
    title = models.CharField(max_length=100)
    photo = models.CharField(max_length=400)
    amount = models.CharField(max_length=100)
    PHOTOGRAPHER=models.ForeignKey(Photographer,on_delete=models.CASCADE)


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    photo = models.CharField(max_length=400)
    dob = models.DateField()
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)



class Booking(models.Model):
    date = models.DateField()
    status=models.CharField(max_length=100)
    CATEGORY=models.ForeignKey(Category,on_delete=models.CASCADE)
    from_d=models.DateField()
    to_d=models.DateField()
    description=models.CharField(max_length=100)
    PHOTOGRAPHER=models.ForeignKey(Photographer,on_delete=models.CASCADE)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)


class Blogs(models.Model):
    date = models.DateField()
    title=models.CharField(max_length=50)
    blog = models.CharField(max_length=5000)
    image = models.CharField(max_length=300,default="no image")
    PHOTOGRAPHER=models.ForeignKey(Photographer,on_delete=models.CASCADE)



class Orders_Main(models.Model):
    date = models.DateField()
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    CONTENT=models.ForeignKey(Contents,on_delete=models.CASCADE,default=1)
    status=models.CharField(max_length=20,default='pending')


class Orders_Sub(models.Model):
    CONTENT=models.ForeignKey(Contents,on_delete=models.CASCADE)
    amount=models.CharField(max_length=100)

class bank(models.Model):
    AcNO = models.CharField(max_length=10)
    balance = models.FloatField(default=10000)


class Payment(models.Model):
    ORDER=models.ForeignKey(Orders_Main,on_delete=models.CASCADE)


class Feedback(models.Model):
    date = models.DateField()
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    type=models.CharField(max_length=100)
    Feed_back=models.CharField(max_length=100)

































