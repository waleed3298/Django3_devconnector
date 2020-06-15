from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Developer(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(null=True,default='devconnector/images/nopic1.png' ,blank=True, upload_to='media/devconnector/images')
    email = models.EmailField(null=True , blank=True)
    bio  = models.TextField(blank=True , null=True)
    fb_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)
    Linked_in = models.URLField(blank=True)
    Personal_site = models.URLField(blank=True)
    github_id = models.CharField(max_length=150,null=True,blank=True)
    skills = models.TextField(blank=True,null=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    role = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE,null=True)
    slug = models.SlugField(null=True,blank = True, default='name', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def __str__(self):
        return self.name

class Education(models.Model):
    Degree_name = models.CharField(max_length=100,null=True,blank=True)
    Institute = models.CharField(max_length=250,null=True,blank=True)
    date_started = models.DateField(null=True)
    date_completed = models.DateField(null=True,blank=True)
    currently = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE,null=True)
    def __str__(self):
        return self.Degree_name

class Experience(models.Model):
    company = models.CharField(max_length=100,blank=True)
    position = models.CharField(max_length=100,null=True)
    date_started_w = models.DateField(null=True)
    date_completed_w = models.DateField(null=True,blank=True)
    currently_w = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE,null=True)

    def __str__(self):
        return self.company

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,null=True)
    text = models.TextField(blank=True)
    name = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments", blank=True)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    p_id = models.IntegerField(null=True)



    def __str__(self):
        return self.text
