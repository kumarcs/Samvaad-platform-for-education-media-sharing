from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

CATEGORY_CHOICES = (
 ('intership','Internship'),
 ('scholarship','Scholarship'),
 ('programmes', 'Programmes'),
    ('other', 'Other'),

)

ACCESS_CATEGORY = (
    ('students', 'Students'),
    ('faculty_and_professors', 'Faculty_and_Professors'),
    ('all', 'All'),
)

class User_Table(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.PROTECT)
    institute_name_user = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    profile_pic_path = models.ImageField(upload_to='profile_pic', default='samvad\media\big.jpg')
    skill_set = models.CharField(max_length=1000)
    access_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_name)


class Institute(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.PROTECT)
    institute_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    institute_type = models.CharField(max_length=100)
    institute_profile_pic_path = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    director_pic_path = models.CharField(max_length=50)

    def __str__(self):
        return str(self.institute_name)

class Newsfeed(models.Model):
    number = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    news_feed_type =  models.CharField(max_length=100,choices=CATEGORY_CHOICES,default='other')
    date =  models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=100)
    intended_for = models.CharField(max_length=50, choices=ACCESS_CATEGORY, default='all')

    def __str__(self):
        return str(self.user_name)

class Societies(models.Model):
    instite_name = models.ForeignKey('Institute',  on_delete=models.PROTECT)
    society = models.CharField(max_length=50)
    profile_pic_path = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return instite_name


class Intersts(models.Model):
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
    interest_type = models.CharField(max_length=50)


class Scholarship(models.Model):
    user_name = models.ForeignKey(User,  on_delete=models.PROTECT)
    status =  models.CharField(max_length=50)
    info =  models.CharField(max_length=100)
    category =  models.CharField(max_length=100)
    upload_date =  models.CharField(max_length=50)
    expir_date =  models.CharField(max_length=50)
    description =  models.CharField(max_length=1000)

class Internship(models.Model):
    user_name = models.ForeignKey(User,  on_delete=models.PROTECT)
    status =  models.CharField(max_length=50)
    info =  models.CharField(max_length=100)
    category =  models.CharField(max_length=100)
    upload_date =  models.CharField(max_length=50)
    expir_date =  models.CharField(max_length=50)
    description =  models.CharField(max_length=1000)

class Project(models.Model):
    user_name = models.ForeignKey(User,  on_delete=models.PROTECT)
    status =  models.CharField(max_length=50)
    info =  models.CharField(max_length=100)
    category =  models.CharField(max_length=100)
    upload_date =  models.CharField(max_length=50)
    expir_date =  models.CharField(max_length=50)
    description =  models.CharField(max_length=1000)


class FriendRequest(models.Model):
    sender_user_name = models.CharField(max_length=100)
    receiver_user_name = models.CharField(max_length=100)
    status = models.CharField(max_length=1000)

class Friend(models.Model):
    sender_user_name = models.CharField(max_length=100)
    receiver_user_name =models.CharField(max_length=100)

class Comment(models.Model):
    post = models.ForeignKey('Newsfeed',  related_name='comments', on_delete=models.PROTECT)
    user_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.description
