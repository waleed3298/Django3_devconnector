from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import Developer,Education,Experience,Posts,Comments
from django.contrib.auth.decorators import login_required
from .forms import DashboardForm , ExperienceForm , EducationForm , PostForm,CommentForm
import datetime

def home(request):
    return render(request,'devconnector/home.html')

def signupuser(request):
    if request.method =='GET':
        return render(request,'devconnector/signupuser.html',{'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request , user)
                return redirect('Dashboard')
            except IntegrityError:
                return render(request,'devconnector/signupuser.html',{'error':'Username already exists'})
        else:
            return render(request,'devconnector/signupuser.html',{'error1':"Passwords didn't match!"})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'devconnector/loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request , username=request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request,'devconnector/loginuser.html',{'form':AuthenticationForm(),'error':'Username or password incorrect'})
        else:
            login(request,user)
            return redirect('Dashboard')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def dashboard(request):
    profiles = Developer.objects.filter(user = request.user)
    works = Experience.objects.filter(user = request.user)
    edu = Education.objects.filter(user = request.user)
    User = request.user
    return render(request,'devconnector/dashboard.html',{'profiles':profiles,'works':works,'edu':edu,'user':User})

@login_required
def CreateProfile(request):
    if request.method == 'GET':
        return render(request,'devconnector/createprofile.html',{'form':DashboardForm()})

    else:
        try:
            form = DashboardForm(request.POST,request.FILES)
            profiles = form.save(commit=False)
            profiles.user = request.user
            profiles.save()
            return redirect('Dashboard')
        except ValueError:
            return render(request,'devconnector/createprofile.html',{'form':DashboardForm(),'error':'Bad data passing'})

@login_required
def EditProfile(request , profile_pk):
    profiles = get_object_or_404(Developer, user = request.user , pk=profile_pk)
    if request.method == 'GET':
        form = DashboardForm(instance = profiles)
        return render(request,'devconnector/editprofile.html',{'profiles':profiles,'form':DashboardForm()})
    else:
        try:
            form = DashboardForm(request.POST ,request.FILES,instance=profiles )
            profile = form.save(commit=False)
            profile.save()
            return redirect('Dashboard')
        except ValueError:
            return render(request , 'devconnector/editprofile.html/' , {'form' : DashboardForm(), 'error' : 'Bad data passing!'})

@login_required
def AddExperience(request):
    if request.method == 'GET':
        return render(request,'devconnector/addexperience.html' , {'form':ExperienceForm()})
    else:
        try:
            form = ExperienceForm(request.POST)
            new_exp = form.save(commit=False)
            new_exp.user = request.user
            new_exp.save()
            return redirect('Dashboard')
        except ValueError:
                return render(request,'devconnector/addexperience.html' , {'form':ExperienceForm(),'error':'Bad Data passing'})

@login_required
def AddEducation(request):
    if request.method == 'GET':
        return render(request,'devconnector/addeducation.html' , {'form':EducationForm()})
    else:
        try:
            form = EducationForm(request.POST)
            new_edu = form.save(commit=False)
            new_edu.user = request.user
            new_edu.save()
            return redirect('Dashboard')
        except ValueError:
                return render(request,'devconnector/addeducation.html' , {'form':EducationForm(),'error':'Bad Data passing'})

@login_required
def deleteprofile(request , profile_pk):
    dp = get_object_or_404(Developer , pk=profile_pk , user=request.user)
    if request.method == 'POST':
        dp.delete()
        return redirect('Dashboard')

@login_required
def deleteexperience(request,work_pk):
    ex = get_object_or_404(Experience , pk=work_pk , user=request.user)
    if request.method == 'POST':
        ex.delete()
        return redirect('Dashboard')

@login_required
def deleteeducation(request , school_pk):
    edu = get_object_or_404(Education , pk=school_pk , user=request.user)
    if request.method == 'POST':
        edu.delete()
        return redirect('Dashboard')

def Developers(request):
    profiles = Developer.objects.order_by('name')
    return render(request,'devconnector/developers.html',{'profiles':profiles})


def Developerinfo(request , the_slug):
    profiles = get_object_or_404(Developer , slug=the_slug)
    skills = profiles.skills.split()
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
    if not profiles.slug:
        profiles.slug = profiles.name
    experience = Experience.objects.filter(user = profiles.user)
    education =  Education.objects.filter(user = profiles.user)
    return render(request,'devconnector/developerinfo.html',{'profiles':profiles,'experience':experience,'education':education,'skills':skills})

@login_required
def viewposts(request):
    profile = Developer.objects.get(user = request.user)
    profile_a = Developer.objects.all()
    posts = Posts.objects.order_by('-date')
    if request.method == 'GET':
        return render(request , 'devconnector/posts.html',{'form':PostForm(),'posts':posts,'profiles':profile,'profile_a':profile_a})
    else:
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.user = request.user
        post.name = profile.name
        post.save()
        return redirect('posts')

@login_required
def comment(request , post_pk):
    profiles = Developer.objects.all()
    posts = get_object_or_404(Posts , pk=post_pk)
    comments = Comments.objects.filter(p_id = post_pk).order_by('-date')
    if request.method == 'GET':
        return render(request,'devconnector/comment.html',{'posts':posts,'comments':comments,'profiles':profiles,'form':CommentForm()})
    else:
        form = CommentForm(request.POST)
        cmnt = form.save(commit=False)
        cmnt.user = request.user
        cmnt.p_id = post_pk
        cmnt.image= 'devconnector/nopic1.png'
        cmnt.save()
        return redirect('posts')

@login_required
def DeleteComment(request , post_pk):
    dc = get_object_or_404(Comments,pk = post_pk)
    if request.method == 'POST' :
            dc.delete()
            return redirect('posts')

@login_required
def DeletePost(request , post_pk):
    dc = get_object_or_404(Posts,pk = post_pk)
    if request.method == 'POST' :
            dc.delete()
            return redirect('posts')
