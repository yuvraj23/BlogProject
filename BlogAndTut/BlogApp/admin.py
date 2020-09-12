from django.contrib import admin
from .models import BlogPost1,Comment,RequestForCode,ProblemStatement,Comment_Related_To_Problem,OffCampusRecruitment

# Register your models here.


@admin.register(BlogPost1)
class BlogPostAdmin(admin.ModelAdmin):
    list_display=['id','title','author','body','publish','created','update','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields=('title','body')
    date_hierarchy='publish'
    ordering=['status','publish']
    raw_id_fields=('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','body')





@admin.register(RequestForCode)
class RequestForCodeAdmin(admin.ModelAdmin):
    list_display=['user','email','Message','ProblemStatement']


@admin.register(ProblemStatement)
class ProblemStatementAdmin(admin.ModelAdmin):
    list_display=['id','title','coder','problemDescription','publish','created','update']
    prepopulated_fields={'slug':('title',)}
    list_filter=('coder','created','publish')
    search_fields=('title','problemDescription')
    date_hierarchy='publish'
    ordering=['publish',]
    raw_id_fields=('coder',)



@admin.register(Comment_Related_To_Problem)
class Comment_Related_To_ProblemAdmin(admin.ModelAdmin):
    list_display=['question','email','reply','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('question','body')


@admin.register(OffCampusRecruitment)
class OffCampusRecruitmentAdmin(admin.ModelAdmin):
    list_display=['title','adminName','description','job_created','job_updated','open']
    list_filter=('title','job_created','job_updated','open')
    search_fields=('description','title')
