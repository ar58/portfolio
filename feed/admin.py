from django.contrib import admin
from .models import Intro,About,Skill, Work, Footer,Contact
# Register your models here.

@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    fields =('greetings','name_intro','name','profession','fb','github','linked_in','head_image')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    pass
