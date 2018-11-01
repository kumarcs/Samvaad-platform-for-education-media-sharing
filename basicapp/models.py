from django.db import models

from django.contrib.auth.models import User


class User_Table(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.PROTECT)
    institute_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    profile_pic_path = models.CharField(max_length=50)
    desc_internship = models.CharField(max_length=1000)
    desc_scholarship = models.CharField(max_length=50)
    desc_project = models.CharField(max_length=50)
    skill_set = models.CharField(max_length=1000)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user_name)


class Institute(models.Model):
    user_name = models.CharField(max_length=50)
    institue_name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    institute_type = models.CharField(max_length=100)
    institute_profile_pic_path = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    director_pic_path = models.CharField(max_length=50)

class Societies(models.Model):
    instite_name = models.ForeignKey('Institute',  on_delete=models.PROTECT)
    society = models.CharField(max_length=50)
    profile_pic_path = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Intersts(models.Model):
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
    interest_type = models.CharField(max_length=50)

class Scholarship(models.Model):
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
    status =  models.CharField(max_length=50)
    info =  models.CharField(max_length=100)
    category =  models.CharField(max_length=100)
    upload_date =  models.CharField(max_length=50)
    expir_date =  models.CharField(max_length=50)
    description =  models.CharField(max_length=1000)

class Internship(models.Model):
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
    status =  models.CharField(max_length=50)
    info =  models.CharField(max_length=100)
    category =  models.CharField(max_length=100)
    upload_date =  models.CharField(max_length=50)
    expir_date =  models.CharField(max_length=50)
    description =  models.CharField(max_length=1000)

class Project(models.Model):
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
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


class Newsfeed(models.Model):
    number = models.CharField(max_length=50)
    user_name = models.ForeignKey('User_Table',  on_delete=models.PROTECT)
    interest =  models.CharField(max_length=100)
    date =  models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=100)


class Comments(models.Model):
    user_name = models.ForeignKey('Newsfeed',  on_delete=models.PROTECT)
    number = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
