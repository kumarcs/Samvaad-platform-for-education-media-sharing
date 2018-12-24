from django.contrib import admin
from basicapp.models import (User_Table, Institute, Newsfeed,Internship,Scholarship,
        Project,Comment, Interest, User_Interest, NewsfeedScore)

# Register your models here.
admin.site.register(User_Table)
admin.site.register(Institute)
admin.site.register(Newsfeed)
admin.site.register(Internship)
admin.site.register(Scholarship)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Interest)
admin.site.register(User_Interest)
admin.site.register(NewsfeedScore)
