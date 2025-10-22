from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals

# Create your models here.
class User(AbstractUser):
    options=(
        ('student','student'),
        ('instructor','instructor'),
    )
    role=models.CharField(max_length=100,choices=options,default="student")

class InstructorProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="instructor")
    profile_pic=models.ImageField(upload_to="profile_picture",null=True,blank=True,default="profile_picture/default.jpg")
    expertise=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender,instance,created,**kwargs):
    if created and instance.role=="instructor":
        InstructorProfile.objects.create(user=instance)
signals.post_save.connect(create_profile,User)


class Category(models.Model):
    catogory_name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.catogory_name
    

class Course(models.Model):
    

    