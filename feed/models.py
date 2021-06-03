from django.db import models


# Create your models here.

class Intro(models.Model):
    greetings   = models.CharField(max_length=160) 
    name_intro  =  models.CharField(max_length=160, default="I'm")
    name        = models.CharField(max_length=50, default='Arindam')
    head_image  = models.ImageField(upload_to = 'media', null=True)

    fb          = models.CharField(max_length=264, default="https://www.facebook.com/ar58p/")
    github      = models.CharField(max_length=264, default="https://github.com/ar58")
    linked_in   = models.CharField(max_length=264, default="https://www.linkedin.com/in/arindam-paul-314165120/")

    def __str__(self):
        return self.name

class About(models.Model):
    title   = models.CharField(max_length=260, default="Arindam Here,")
    text    = models.TextField(default= ' ')
    about_image = models.ImageField(upload_to = 'media', null=True)

class Skill(models.Model):
    title = models.CharField(max_length=260, default='Professional Skills')
    text = models.TextField(default= ' ')
    image = models.ImageField(upload_to = 'media')

class Work(models.Model):
    work_image = models.ImageField(upload_to='media')

class Contact(models.Model):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    message = models.TextField(default=' ')

    def __str__(self):
        return self.name
    

class Footer(models.Model):
    title = models.CharField(max_length=260)
    copyright = models.TextField(default=' ')
    instagram = models.CharField(max_length=260)
    twitter = models.CharField(max_length=260)