from django.shortcuts import render
from django.template import loader

from basicapp.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basicapp.models import (User_Table, Newsfeed, Institute, Internship,
                            Project, Interest, User_Interest, NewsfeedScore)
from django.db.models import Q
from basicapp.forms import UserForm, UserProfileInfoForm, InstituteProfileInfoForm, addUserForm, addNewsFeedForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (View, TemplateView,
                                   ListView, DetailView,
                                   CreateView, UpdateView,
                                   DeleteView)


from django.db import connection
from django.shortcuts import redirect
import paralleldots
paralleldots.set_api_key("ghdY3NjkLKVI2uE5i3CK0hkpfWugfO9HATYIX9P8kJc")

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('Loginned ')
                n1 = User_Table.objects.filter(user_name__username__icontains=username)
                print(n1[0].access_type)
            if n1[0].access_type == 'InstituteAdmin':
                return HttpResponseRedirect(reverse('instituteAdmin'))
            elif n1[0].access_type == 'SuperAdmin':
                return HttpResponseRedirect(reverse('superAdmin'))
            elif n1[0].access_type == 'NormalUser':
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print('someone tried login and failed')
            print('username : {} and password {}'.format(username, password))
            return HttpResponse("invalid comb of username password")
    else:
        return render(request, 'basicapp/login.html', {})



@login_required
def index(request):
    n3 = User_Interest.objects.filter(user_name__username__icontains=request.user.username)

    n2= Newsfeed.objects.all()
    interestOne = NewsfeedScore.objects.filter(category=n3[0].interest_name).filter(score__gte=0.85)
    interestTwo = NewsfeedScore.objects.filter(category=n3[1].interest_name).filter(score__gte=0.85)
    interestThree = NewsfeedScore.objects.filter(category=n3[2].interest_name).filter(score__gte=0.85)

    #attempting to make one of all query
    #interestedNewsfeed = NewsfeedScore.objects.filter(Q(category=n3[0].interest_name) | Q(category=n3[1].interest_name) | Q(category=n3[2].interest_name)).filter(score__gte=0.85)
    print(interestOne)
    n1 = User_Table.objects.filter(user_name__username__icontains=request.user.username)
    return render(request, 'basicapp/index.html', {'user_record':n1, 'first_two_news_feed':n2[0:2], 'interestOneFeed':interestOne, 'interestTwoFeed':interestTwo, 'interestThreeFeed':interestThree, 'rest_news_feed':n2[2:]})

@login_required
def instituteAdmin(request):
    n2= Newsfeed.objects.all()
    return render(request, 'basicapp/instituteAdmin.html',{'news_feed':n2,})


@csrf_protect
def superAdmin(request):

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)
        institute_form = InstituteProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user_name = user

            profile.save()

            institute = institute_form.save(commit=False)
            institute.user_name = user
            institute.save()

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        institute_form = InstituteProfileInfoForm()

    return render(request, 'basicapp/superAdmin.html', {'user_form':user_form, 'profile_form':profile_form, 'institute_form': institute_form})

def addUser(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        add_user_form = addUserForm(data = request.POST)

        if user_form.is_valid() and add_user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = add_user_form.save(commit=False)
            profile.user_name = user
            profile.access_type = 'NormalUser'
            profile.save()

        else:
            print(user_form.errors, add_user_form.errors)
    else:
        user_form = UserForm()
        add_user_form = addUserForm()

    return render(request, 'basicapp/adduser.html', {'user_form':user_form, 'add_user_form':add_user_form})

def addNewsFeed(request):
    print('here')
    n1 = User_Table.objects.filter(user_name__username__icontains=request.user.username)
    if request.method == 'POST':
        print('inside POST')
        add_news_feed = addNewsFeedForm(data = request.POST)
        if add_news_feed.is_valid():
            news_feed = add_news_feed.save(commit=False)
            news_feed.user_name = request.user.username
            news_feed.save()

            category = { "Sports":['Cricket', 'Football', 'Soccer', 'Swimming', 'Horse Riding', 'Table Tennis', 'Badminton'], 'Artificial Intelligence':['Machine Learning', 'Deep Learning', 'Mimic', 'Linear Regression', 'Logistic Regression'], 'Internet of Things': ['Automation', 'Alexa', 'Siri', 'Google Home'], 'Data Structure and Algorithms':['DFS', 'BFS', 'Array', 'Stacks', 'Queues', 'Recursion', 'Disjoint Set'], 'Competitive Programming':['Codechef', 'Hackerearth', 'Hackerrank', 'Purple'],
            'Management':['Event', 'Time'], 'Developer':['Software Engineering', 'Project', 'APIs', 'Web Development'], 'Blockchain':['Cryptocurrency', 'Bitcoins', 'Etherium'], 'Operting System':[], 'Art':[], 'Gaming':[], 'Virtual Reality':[], 'Microprocessors':[], 'Aviation':[], 'Mechanical Engineering':[], 'Electronics Engineering':[], 'Textile Engineering':[], 'Mining Engineering':[]}

            api_scores = paralleldots.custom_classifier(request.POST.get('description'), category);
            print(request.POST.get('description'))
            print(api_scores)
            for api_score in api_scores['taxonomy']:
                tag = api_score['tag']
                score = api_score['confidence_score']
                score_table = NewsfeedScore()
                score_table.newsfeed = news_feed
                score_table.category = tag
                score_table.score = score
                score_table.save()

            return index(request)
        else:
            print(news_feed.errors)
    else:
        add_news_feed_form = addNewsFeedForm()

    print('here after')
    return render(request, 'basicapp/addnewsfeed.html', {'add_news_feed_form':add_news_feed_form,'user_record':n1})

#will do later for handling interest of user inputted by user itself
# added on 24_DEC
@csrf_exempt
def addUserInterest(request):
    template = loader.get_template('basicapp/addUserInterest.html')
    if request.method == 'GET':
        return HttpResponse(template.render())
    else:
        input_username = User.objects.get(id=request.user.id)
        input_interest = request.POST.get('user_interest')
        user_interest = User_Interest()
        user_interest.user_name = input_username
        user_interest.interest_name = input_interest
        user_interest.save()
        return HttpResponse("interest added")

class NewsFeedDetail(DetailView):
    context_object_name= 'newsfeed_detail'
    model=Newsfeed
    template_name= 'basicapp/feed_details.html'

def userAccountInfo(request):
    n1 = Internship.objects.filter(user_name__username__icontains = request.user.username)
    n2 = Project.objects.filter(user_name__username__icontains = request.user.username)
    n3 = User_Interest.objects.filter(user_name__username__icontains = request.user.username)
    return render(request, 'basicapp/UserProfilePage.html', {'internships': n1, 'projects': n2, 'interests': n3})

@login_required
def instituteprofilepage(request):
    return render(request, 'basicapp/InstituteProfilePage.html')

@login_required
def InstituteExtra(request):
    return render(request, 'basicapp/InstituteExtras.html')


@login_required
def institutesocities(request):
    return render(request, 'basicapp/InstituteSocities.html')

@login_required
def internships(request):
    feed=Newsfeed.objects.filter(news_feed_type__exact = 'internship')
    return render(request, 'basicapp/UserExtras.html', {'feed':feed})

def scholarships(request):
    feed=Newsfeed.objects.filter(news_feed_type__exact = 'scholarship')
    return render(request, 'basicapp/UserExtras.html', {'feed':feed})

def programmes(request):
    feed = Newsfeed.objects.filter(news_feed_type__exact = 'programmes')
    return render(request, 'basicapp/UserExtras.html', {'feed':feed})

def add_comment_to_post(request, pk):
    post = Newsfeed.objects.get(pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post=post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'basicapp/add_comment_to_post.html', {'form': form})
