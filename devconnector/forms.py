from django.forms import ModelForm
from django import forms
from .models import Developer , Experience,Education , Posts , Comments

class DashboardForm(ModelForm):
    class Meta:
        model = Developer
        fields = ['name','image','bio','fb_link','insta_link','Linked_in','Personal_site','github_id','skills','role','company','email']

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['company','position','date_started_w','date_completed_w','currently_w']

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['Degree_name','Institute','date_started','date_completed','currently']

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['text']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user' , 'text']
